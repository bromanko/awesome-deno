# Single-entry integration example

Saved research reused for one correction; no new entry research and no full-catalog freshness run. Real production history collection, Opus history review, patch/link checks and report rendering were exercised.

**1 ready for review · 0 held**

1 checked · 0 unchanged · 1 saved assessment reused · 0 source checks unavailable

<h2>clite — Ready for maintainer review</h2>

```diff
--- a/README.md
+++ b/README.md
@@ -79,7 +79,7 @@
 - [charmd](https://github.com/littletof/charmd) - A simple, extendable markdown renderer for your terminal.
 - [cli-spinner](https://github.com/ameerthehacker/deno-cli-spinners) - Show spinners in the terminal while running long tasks.
 - [cliffy](https://github.com/c4spar/cliffy) - The complete solution for building interactive command-line tools.
-- [clite](https://github.com/jersou/clite-parser) - Automatic CLI generation from a class.
+- [clinfer](https://github.com/jersou/clinfer) - Automatic CLI generation from a class.
 - [commit-sage-cli](https://github.com/AhmedOsman101/commit-sage-cli) - Generates Conventional Commit messages with AI based on Git repository changes.
 - [tui](https://github.com/Im-Beast/deno_tui) - Module which allows easy creation of Terminal User Interfaces.
 - [yargs](https://github.com/yargs/yargs) - The modern, pirate-themed successor to optimist.
```

<details>
<summary>Evidence and checks</summary>

<p>The project was renamed. github.com/jersou/clite-parser redirects (the API returns &#x27;Moved Permanently&#x27;) to jersou/clinfer. The changelog records &#x27;rename clite-parser to cli-from&#x27; (0.9.0) and then &#x27;rename the project to clinfer&#x27; (0.9.3). deno.json now names the package @jersou/clinfer. The description still holds: classes are still supported, and objects/ES modules are additions. &#x27;clinfer&#x27; sorts between &#x27;cliffy&#x27; and &#x27;commit-sage-cli&#x27;, the same position as &#x27;clite&#x27;, so the order does not change.</p>

<p>https://api.github.com/repos/jersou/clite-parser — The API returns &#x27;Moved Permanently&#x27;. The packet snapshot also resolves the repository to jersou/clinfer (not archived).</p>

<p>https://raw.githubusercontent.com/jersou/clinfer/main/deno.json — name &#x27;@jersou/clinfer&#x27;, version 0.9.9, exports ./mod.ts.</p>

<p>https://raw.githubusercontent.com/jersou/clinfer/main/docs/CHANGELOG.md — 0.9.3 (2026-05-29): &#x27;rename the project to clinfer (CLI inference)&#x27;. 0.9.0: &#x27;rename clite-parser to cli-from&#x27;.</p>

<p>https://raw.githubusercontent.com/jersou/clinfer/main/README.md — The README reads &#x27;clinfer brings CLI inference to Node, Deno, and Bun. Pass it an object, a class, an ES module or a function&#x27;. Install: &#x27;deno add jsr:@jersou/clinfer&#x27;.</p>

<p>Caveats: The description &#x27;Automatic CLI generation from a class.&#x27; remains accurate. Widening it to objects and modules is optional.</p>

<p>related: The search covered 8 queries across denolib/awesome-deno and bromanko/awesome-deno for &#x27;clite&#x27;, &#x27;clinfer&#x27; and both repository URLs. It completed with no errors. Two records came back, and neither proposes or rejects the rename to clinfer. PR #392 (https://github.com/denolib/awesome-deno/pull/392) is the merged PR that first added the current entry, &#x27;[clite](https://github.com/jersou/clite-parser) - Automatic CLI generation from a class.&#x27; A maintainer approved it (https://github.com/denolib/awesome-deno/pull/392#pullrequestreview-2327236400). It is background for this entry, not an earlier version of this correction. PR #378 (https://github.com/denolib/awesome-deno/pull/378) was an earlier attempt to add clite-parser and was closed without merging. The maintainer&#x27;s objection was that the project was &#x27;too new&#x27; and needed more adoption (https://github.com/denolib/awesome-deno/pull/378#issuecomment-1909618481). That objection was about whether to list the project at all, and #392 later resolved it by adding the entry. It does not apply to updating the name and URL after the rename. No open PR proposes the clite-parser → clinfer change, and no merged PR has already made it. Checks passed; existing unrelated link failures are listed separately.</p>

</details>

<details>
<summary>Saved review baseline</summary>

0 new completed reviews · 1 pending.

To retain completed reviews, review and commit the bundled `baseline.json` as `.um/freshness/baseline.json`.

</details>

<details>
<summary>Full research and run details</summary>

# Freshness research

Advisory only; every suggested change requires maintainer review.
No list edits, PRs, comments, or reviews were submitted.

Catalog revision: `3422b89aafff49aa56827880b9b7f588ad5416d9`
Scope: one selected entry from saved research
Catalog recheck: unchanged

Sources below are agent-reported observations, not independent verification.

## Entry 82

<pre>clite

The project was renamed. github.com/jersou/clite-parser redirects (the API returns &#x27;Moved Permanently&#x27;) to jersou/clinfer. The changelog records &#x27;rename clite-parser to cli-from&#x27; (0.9.0) and then &#x27;rename the project to clinfer&#x27; (0.9.3). deno.json now names the package @jersou/clinfer. The description still holds: classes are still supported, and objects/ES modules are additions. &#x27;clinfer&#x27; sorts between &#x27;cliffy&#x27; and &#x27;commit-sage-cli&#x27;, the same position as &#x27;clite&#x27;, so the order does not change.

https://api.github.com/repos/jersou/clite-parser
The API returns &#x27;Moved Permanently&#x27;. The packet snapshot also resolves the repository to jersou/clinfer (not archived).
https://raw.githubusercontent.com/jersou/clinfer/main/deno.json
name &#x27;@jersou/clinfer&#x27;, version 0.9.9, exports ./mod.ts.
https://raw.githubusercontent.com/jersou/clinfer/main/docs/CHANGELOG.md
0.9.3 (2026-05-29): &#x27;rename the project to clinfer (CLI inference)&#x27;. 0.9.0: &#x27;rename clite-parser to cli-from&#x27;.
https://raw.githubusercontent.com/jersou/clinfer/main/README.md
The README reads &#x27;clinfer brings CLI inference to Node, Deno, and Bun. Pass it an object, a class, an ES module or a function&#x27;. Install: &#x27;deno add jsr:@jersou/clinfer&#x27;.

Blocking uncertainties:
None reported.

Informational caveats:
The description &#x27;Automatic CLI generation from a class.&#x27; remains accurate. Widening it to objects and modules is optional.

Recommendation: update
Proposed name: clinfer
Proposed URL: https://github.com/jersou/clinfer
Proposed description: None</pre>


</details>

Proposals only; no catalog edits or PRs submitted. Full records and checked patches are in the run artifacts.
