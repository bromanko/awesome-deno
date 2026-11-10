"""Catalog-specific collection and patch preservation boundaries."""
import hashlib
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import ci
import catalog

class AdapterTests(unittest.TestCase):
    def proposal(self,text,**changes):
        entries=ci.entries(text)
        row=dict(id=entries[0]['id'],action='update',reason='Verified identity.', evidence=[dict(url='https://example.com',observation='Official source')], limitations=[],blockers=[],newName=None,newUrl='https://example.com/new',newDescription=None)
        row.update(changes)
        data=dict(entries=[entries[0]],readme=text,readmeHash=hashlib.sha256(text.encode()).hexdigest(),catalogSha='a'*40)
        return ci.previews(data,dict(results=[row]),'unchanged')[0]

    def test_actual_catalog_coverage(self):
        readme=Path('README.md').read_text()
        rows=ci.entries(readme)
        candidates=[line for line in readme.splitlines() if ci.BULLET.match(line) and ('http://' in line or 'https://' in line)]
        self.assertEqual(len(rows),len(candidates))
        self.assertEqual(len({catalog.key(e) for e in rows}),len(rows))

    def test_markers_indentation_bare_and_nested_labels(self):
        text='# Tools\n  * [Tool [EN]](https://example.com)\n* [Other](https://other.example): Description.\n'
        rows=ci.entries(text)
        self.assertEqual(len(rows),2)
        self.assertEqual(rows[0]['name'],'Tool [EN]')
        self.assertEqual(rows[0]['description'],'')
        self.assertIn('+  * [Tool [EN]](https://example.com/new)',self.proposal(text)[0]['patch'])

    def test_metadata_and_en_dash_preserved(self):
        text='* [Tool](https://example.com) – Old text. ([Source Code](https://github.com/example/tool)) `MIT` `Python`\n'
        entry=ci.entries(text)[0]
        self.assertEqual(entry['description'],'Old text.')
        self.assertEqual(entry['sourceUrls'],['https://example.com','https://github.com/example/tool'])
        patch=self.proposal(text,newDescription='New text.')[0]['patch']
        self.assertIn('+* [Tool](https://example.com/new) – New text. ([Source Code](https://github.com/example/tool)) `MIT` `Python`',patch)

    def test_complex_description_and_parent_removal_held(self):
        self.assertEqual(self.proposal('* Tool: [iOS](https://example.com), [Android](https://other.example)\n',newDescription='New text.'),[])
        self.assertEqual(self.proposal('- [Talk](https://example.com)\n  - [Slides](https://other.example)\n',action='remove',newUrl=None),[])

    def test_full_row_metadata_changes_invalidate_claim(self):
        before=ci.entries('* [Tool](https://example.com) - Tool. `MIT`')[0]
        after=ci.entries('* [Tool](https://example.com) - Tool. `GPL`')[0]
        self.assertNotEqual(catalog.claim(before,''),catalog.claim(after,''))

    def test_secondary_source_incomplete_never_baselined(self):
        from unittest.mock import patch
        with patch.object(catalog,'single_snapshot',side_effect=[dict(complete=True,fingerprint='a',source={}),dict(complete=False,error='Unavailable')]):
            self.assertFalse(catalog.snapshot(dict(url='https://a.example',sourceUrls=['https://a.example','https://b.example']))['complete'])

    def test_blank_before_children_and_complex_rename_held(self):
        self.assertEqual(self.proposal('- [Talk](https://example.com)\n\n  - [Slides](https://other.example)\n',action='remove',newUrl=None),[])
        self.assertEqual(self.proposal('* Tool: [iOS](https://example.com), [Android](https://other.example)\n',newName='New Project'),[])

    def test_description_link_is_in_required_destinations(self):
        row=ci.entries('- [Tool](https://example.com) - See [guide](https://guide.example).')[0]
        self.assertEqual(row['sourceUrls'],['https://example.com','https://guide.example'])
