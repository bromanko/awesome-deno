# Catalog review inventory

**31 proposed changes · 10 uncertain · 43 unresolved keeps**

220 entries researched. 136 saved reviews for recurring runs.

Research recommendations from the initial Opus review. The full set has not passed prior-discussion or patch validation. Proposed diffs are previews, not approved patches. Nothing was applied or submitted.

Catalog: `8933090a6daecdd5665a91b39b02bbb8f79d4fdd` · README SHA-256: `89412217ffea71456f9f6fb713d17bc2438666f74b64b32a7ec58fc1c3a4eb07`

## Proposed changes

<h3>clite — update</h3>

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
<summary>Evidence and limitations</summary>

<p>The project was renamed. github.com/jersou/clite-parser redirects (the API returns &#x27;Moved Permanently&#x27;) to jersou/clinfer. The changelog records &#x27;rename clite-parser to cli-from&#x27; (0.9.0) and then &#x27;rename the project to clinfer&#x27; (0.9.3). deno.json now names the package @jersou/clinfer. The description still holds: classes are still supported, and objects/ES modules are additions. &#x27;clinfer&#x27; sorts between &#x27;cliffy&#x27; and &#x27;commit-sage-cli&#x27;, the same position as &#x27;clite&#x27;, so the order does not change.</p>

<p>https://api.github.com/repos/jersou/clite-parser — The API returns &#x27;Moved Permanently&#x27;. The packet snapshot also resolves the repository to jersou/clinfer (not archived).</p>

<p>https://raw.githubusercontent.com/jersou/clinfer/main/deno.json — name &#x27;@jersou/clinfer&#x27;, version 0.9.9, exports ./mod.ts.</p>

<p>https://raw.githubusercontent.com/jersou/clinfer/main/docs/CHANGELOG.md — 0.9.3 (2026-05-29): &#x27;rename the project to clinfer (CLI inference)&#x27;. 0.9.0: &#x27;rename clite-parser to cli-from&#x27;.</p>

<p>https://raw.githubusercontent.com/jersou/clinfer/main/README.md — The README reads &#x27;clinfer brings CLI inference to Node, Deno, and Bun. Pass it an object, a class, an ES module or a function&#x27;. Install: &#x27;deno add jsr:@jersou/clinfer&#x27;.</p>

<p>Caveats: The description &#x27;Automatic CLI generation from a class.&#x27; remains accurate. Widening it to objects and modules is optional.</p>

<p>Independent source check: Official redirect, changelog, package identity and current README confirm the rename to clinfer. CLI generation from classes remains supported; the existing section position remains appropriate.</p>

<p>https://github.com/jersou/clite-parser — Redirects to jersou/clinfer.</p>

<p>https://github.com/jersou/clinfer/blob/main/docs/CHANGELOG.md — May2026 versions record clite-parser→cli-from→clinfer.</p>

<p>https://github.com/jersou/clinfer/blob/main/deno.json — Package @jersou/clinfer version0.9.9.</p>

<p>https://github.com/jersou/clinfer/blob/main/README.md — Deno installation and class-based generation remain documented.</p>

</details>

<h3>commit-sage-cli — remove</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -80,7 +80,6 @@
 - [cli-spinner](https://github.com/ameerthehacker/deno-cli-spinners) - Show spinners in the terminal while running long tasks.
 - [cliffy](https://github.com/c4spar/cliffy) - The complete solution for building interactive command-line tools.
 - [clite](https://github.com/jersou/clite-parser) - Automatic CLI generation from a class.
-- [commit-sage-cli](https://github.com/AhmedOsman101/commit-sage-cli) - Generates Conventional Commit messages with AI based on Git repository changes.
 - [tui](https://github.com/Im-Beast/deno_tui) - Module which allows easy creation of Terminal User Interfaces.
 - [yargs](https://github.com/yargs/yargs) - The modern, pirate-themed successor to optimist.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The project&#x27;s own documentation shows it has moved off Deno. A plan document, &#x27;Port remaining Deno runtime and release tooling to Bun&#x27;, has the status &#x27;Landed in v3.0.0 (2026-10-10, PR #68)&#x27;. ADR 0015 commits to &#x27;Bun-native APIs first&#x27;. Current package.json pins engines.bun 1.4.3 and depends on @types/bun, and deno.json is no longer on main. The tool is now distributed as Bun-compiled binaries. The commit-message description is still accurate, but the listed implementation no longer has a Deno interface or runtime relevance.</p>

<p>https://raw.githubusercontent.com/AhmedOsman101/commit-sage-cli/main/docs/plans/2026-10-10-port-remaining-bun-runtime.md — Title &#x27;Port remaining Deno runtime and release tooling to Bun&#x27;. Status: &#x27;Landed in v3.0.0 (2026-10-10, PR #68)&#x27;. It describes deleting deno.lock and the remaining Deno.* usage.</p>

<p>https://raw.githubusercontent.com/AhmedOsman101/commit-sage-cli/main/docs/adr/015-bun-native-first.md — ADR 0015: &#x27;Bun-native APIs first, node:* only where Bun has none&#x27;.</p>

<p>https://raw.githubusercontent.com/AhmedOsman101/commit-sage-cli/main/package.json — version 3.2.1, engines { bun: 1.4.3 }, devDependencies include @types/bun. Cliffy is pulled from npm:@jsr. No Deno manifest.</p>

<p>https://raw.githubusercontent.com/AhmedOsman101/commit-sage-cli/main/README.md — Requirements list Git and &#x27;Bun 1.4.x only if compiling from source&#x27;. Deno is not mentioned. Install options are prebuilt binaries, an installer script and AUR.</p>

<p>Caveats: Versions before 3.0.0 were Deno-based and may still exist in releases. Their maintenance status is unknown and was not inferred.; The project itself is active and works as a commit-message generator. Removal is proposed only because it is no longer Deno-related.</p>

<p>Independent source check: The current release moved its runtime and build tooling to Bun. Official completed migration plan, accepted architecture decision and current manifest corroborate this. Removal from a Deno catalog is curator judgment; older Deno releases remain historical context, and their maintenance was not established.</p>

<p>https://github.com/AhmedOsman101/commit-sage-cli/blob/main/docs/plans/2026-10-10-port-remaining-bun-runtime.md — Plan says landed in v3.0.0; Deno runtime and release cutover explicitly scoped.</p>

<p>https://github.com/AhmedOsman101/commit-sage-cli/blob/main/docs/adr/015-bun-native-first.md — Bun-native runtime APIs preferred; node fallbacks where needed.</p>

<p>https://github.com/AhmedOsman101/commit-sage-cli/blob/main/package.json — Version3.2.1, Bun1.4.3 engine; blob7daf5d280d0e2f5b385eb3cbac2c805ce15d5eb3.</p>

<p>https://github.com/AhmedOsman101/commit-sage-cli/blob/main/README.md — Current source-build requirement is Bun; Deno mention is historical port acknowledgment.</p>

</details>

<h3>aws-api — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -85,7 +85,7 @@
 - [yargs](https://github.com/yargs/yargs) - The modern, pirate-themed successor to optimist.
 
 ### Cloud APIs
-- [aws-api](https://aws-api.deno.dev/) - From-scratch Typescript AWS API client built for Deno.
+- [aws-api](https://github.com/cloudydeno/aws-api) - From-scratch Typescript AWS API client built for Deno.
 - [sigflint](https://github.com/bompus/sigflint) - AWS Signature Version 4 and SigV4a request signing with no dependencies, for use with `fetch`.
 
 ### Database
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed host https://aws-api.deno.dev/ permanently redirects (301) to https://aws-api.danopia.deno.net/, the codegen web service. The source repo is github.com/cloudydeno/aws-api, renamed from deno-aws_api (301). Its README tagline is exactly &#x27;From-scratch Typescript AWS API client built for Deno.&#x27; The contribution rules say &#x27;Link to the GitHub repo&#x27;, so the canonical GitHub repo is proposed as the URL. The description stays accurate.</p>

<p>https://aws-api.deno.dev/ — 301 to https://aws-api.danopia.deno.net/, then 302 to /v0.5/services/ (HTTP 200).</p>

<p>https://aws-api.danopia.deno.net/v0.5/services/ — &#x27;AWS API Client Codegen&#x27; service page. It links to github.com/cloudydeno/deno-aws_api and the examples import jsr:@cloudydeno/aws-api@0.9.0.</p>

<p>https://github.com/cloudydeno/aws-api — github.com/cloudydeno/deno-aws_api returns 301 to this repo. The README reads &#x27;aws_api for Deno — From-scratch Typescript AWS API client built for Deno.&#x27;</p>

<p>Caveats: The other option is to point to https://aws-api.danopia.deno.net/ (the redirect target). Either works. The GitHub repo is proposed because of the contribution rules and because it is less tied to the hosting domain.</p>

<p>Independent source check: The old deno.dev service URL redirects to the new deno.net host. Official rendered repository README confirms identity and Deno API-client purpose. Linking the canonical GitHub repo fits contribution rules. Valid cleanup, less compelling than the rename/runtime examples.</p>

<p>https://aws-api.deno.dev/ — Redirect observed to aws-api.danopia.deno.net/v0.5/services/; official service links source and JSRpackage.</p>

<p>https://github.com/cloudydeno/aws-api — Rendered README identifies AWS API client for Deno. Connector fetch of root README.md returned404; rendered repository content was available.</p>

</details>

<h3>nessie — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -96,7 +96,7 @@
 - [denodb](https://github.com/eveningkid/denodb) - MySQL, SQLite, MariaDB, PostgreSQL and MongoDB ORM for Deno.
 - [dongoose](https://github.com/roonie007/dongoose) - A simple and easy to use ORM for Deno KV.
 - [maxminddb](https://github.com/josh-hemphill/maxminddb-wasm) - A library that enables the usage of MaxmindDB geoIP database files
-- [nessie](https://github.com/halvardssm/deno-nessie) - Create, migrate and rollback migrations for PostgreSQL, MySQL and SQLite.
+- [nessie](https://github.com/lmxrd/deno-nessie) - Create, migrate and rollback migrations for PostgreSQL, MySQL and SQLite.
 - [postgres](https://github.com/denodrivers/postgres) - Driver for PostgreSQL database.
 - [redis](https://github.com/denodrivers/redis) - An experimental implementation of redis client for deno.
 - [yongo](https://github.com/yooneskh/yongo) - Subset of Mongoose api in deno (like populate) but will not fully copy mongoose
```

<details>
<summary>Evidence and limitations</summary>

<p>github.com/halvardssm/deno-nessie now redirects (301) to github.com/lmxrd/deno-nessie. The lmxrd profile belongs to the same author (Halvard Mørstad), and the old halvardssm profile returns 404, so this is an account rename. The JSR package @halvardm/nessie links to lmxrd/deno-nessie. Only the URL needs updating: the README still documents up/down migrations and rollback on SQLite, Postgres and MySQL, so the description stays accurate.</p>

<p>https://github.com/halvardssm/deno-nessie — Returns HTTP 301 to https://github.com/lmxrd/deno-nessie.</p>

<p>https://github.com/lmxrd — The profile title reads &quot;lmxrd (Halvard Mørstad)&quot;. https://github.com/halvardssm returns 404.</p>

<p>https://raw.githubusercontent.com/lmxrd/deno-nessie/main/README.md — &quot;Nessie runs versioned up/down migrations and seeds on SQLite, Postgres and MySQL.&quot; A `rollback` command &quot;Reverts applied migrations&quot;. The badges link to lmxrd/deno-nessie.</p>

<p>https://raw.githubusercontent.com/lmxrd/deno-nessie/main/deno.json — Package name is @halvardm/nessie, version 3.0.0-rc.4. It exports clients for mysql, postgres and sqlite.</p>

<p>https://jsr.io/@halvardm/nessie — The JSR package page links to github.com/lmxrd/deno-nessie.</p>

<p>Caveats: Version 3 is a release candidate built on @stdx/database. I didn&#x27;t run it.</p>

</details>

<h3>fresh — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -106,7 +106,7 @@
 - [Denops](https://github.com/vim-denops/denops.vim) - 🐜 An ecosystem to write Vim/Neovim plugins with Deno.
 
 ### Frontend framework
-- [fresh](https://github.com/denoland/fresh) - The next-gen web framework.
+- [fresh](https://github.com/freshframework/fresh) - The next-gen web framework.
 - [packup](https://github.com/kt3k/packup) - Zero-config web application packager for Deno.
 - [ultra](https://github.com/exhibitionist-digital/ultra) - 💎 Modern Streaming React Framework in Deno.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>github.com/denoland/fresh redirects (301) to github.com/freshframework/fresh. A maintainer post in the repo (Discussion #3830) says Fresh was moved into its own GitHub organization with help from a Deno team member. The URL should be updated. The README still calls Fresh &quot;a next generation web framework&quot;, and @fresh/core 2.3.3 is published from the repo, so the description and the name stay accurate.</p>

<p>https://github.com/denoland/fresh — Returns HTTP 301 to https://github.com/freshframework/fresh.</p>

<p>https://github.com/freshframework/fresh/discussions/3830 — &quot;What&#x27;s next for Fresh?&quot;: &quot;Fresh is now in it&#x27;s own org so that more people can have review and PR access to it... Deno folks will continue to contribute. Fresh will become Vite-only.&quot; It also says this was done &quot;with @bartlomieju&#x27;s help&quot;.</p>

<p>https://raw.githubusercontent.com/freshframework/fresh/main/README.md — &quot;Fresh is a next generation web framework, built for speed, reliability, and simplicity.&quot; The scaffold command is deno run -Ar jsr:@fresh/init.</p>

<p>https://raw.githubusercontent.com/freshframework/fresh/main/packages/fresh/deno.json — @fresh/core version 2.3.3.</p>

<p>Caveats: The usefresh.dev website and the jsr.io/@fresh/core page still link to github.com/denoland/fresh, which redirects.; The maintainers say future work will move Fresh to Vite-only and add runtimes beyond Deno. Deno remains its primary target today.</p>

</details>

<h3>ImageScript — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -115,7 +115,7 @@
 - [sdl2](https://github.com/littledivy/deno_sdl2) - SDL2 module for Deno
 
 ### Image
-- [ImageScript](https://github.com/matmen/ImageScript) - Image processing in JavaScript, utilizing WebAssembly for performance.
+- [ImageScript](https://github.com/imagescript/ImageScript) - Image processing in pure TypeScript with no dependencies.
 - [kavel](https://github.com/hanshs474/kavel-ts) - Generate and edit images with AI without an API key or account.
 - [monke](https://github.com/retraigo/monke) - Color quantization and dithering library with extra image filters (blur, invert, etc).
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The entry has two errors. First, github.com/matmen/ImageScript now redirects (301) to github.com/imagescript/ImageScript, and package.json names imagescript/ImageScript as the repository. Second, the entry says the library uses WebAssembly, but the README now says &quot;pure TypeScript: no WebAssembly, no native binaries, no dependencies&quot;. That makes the WebAssembly claim false. Deno is still supported.</p>

<p>https://github.com/matmen/ImageScript — Returns HTTP 301 to https://github.com/imagescript/ImageScript.</p>

<p>https://raw.githubusercontent.com/imagescript/ImageScript/master/README.md — &quot;ImageScript decodes, edits and encodes images in pure TypeScript: no WebAssembly, no native binaries, no dependencies. It runs in Node.js 22.13+, Deno, Bun, browsers and edge runtimes&quot;. The Deno install command is deno add jsr:@matmen/imagescript.</p>

<p>https://raw.githubusercontent.com/imagescript/ImageScript/master/package.json — name imagescript, version 3.20.2. description: &quot;Pure TypeScript image processing that runs everywhere&quot;. repository.url: git+https://github.com/imagescript/ImageScript.git.</p>

<p>Caveats: The JSR package is still published under the @matmen scope. I didn&#x27;t run the library.</p>

</details>

<h3>netsaur — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -125,7 +125,7 @@
 ### Machine learning
 - [appraisal](https://github.com/retraigo/appraisal) - Feature extraction and conversion.
 - [classy-lala](https://github.com/retraigo/la-classy) - Single-layer perceptrons for supervised learning tasks.
-- [netsaur](https://github.com/denosaurs/netsaur) - Powerful machine learning, accelerated by WebGPU
+- [netsaur](https://github.com/denosaurs/netsaur) - Machine learning library with native CPU and WebAssembly backends.
 
 ### Mail
 - [deno-smtp](https://github.com/manyuanrong/deno-smtp) - A smtp mail sender for deno.
```

<details>
<summary>Evidence and limitations</summary>

<p>Still a Deno ML library (JSR @denosaurs/netsaur) and fits Machine learning, but the listed claim &#x27;accelerated by WebGPU&#x27; isn&#x27;t supported. The official README lists working backends as native CPU (Rust) and WASM, with GPU marked TODO/WIP. The GPU crate that does exist depends on cudarc, which is CUDA, not WebGPU. The proposed wording drops the unsupported claim and adds the missing period.</p>

<p>https://raw.githubusercontent.com/denosaurs/netsaur/main/README.md — Backends section: &#x27;CPU - Native backend written in Rust&#x27;, &#x27;WASM - WebAssembly backend written in Rust&#x27;, &#x27;GPU (TODO)&#x27;. Features list: &#x27;Can run on both the CPU and the GPU (WIP)&#x27;. No WebGPU mention.</p>

<p>https://raw.githubusercontent.com/denosaurs/netsaur/main/crates/core-gpu/Cargo.toml — The netsaur-gpu crate depends on cudarc (CUDA bindings), not a WebGPU implementation.</p>

<p>https://raw.githubusercontent.com/denosaurs/netsaur/main/deno.jsonc — Package @denosaurs/netsaur v0.4.2. Exports core, data, utilities, tokenizers and visualizer. Build tasks cover cpu, gpu (cargo) and wasm.</p>

<p>https://github.com/denosaurs/netsaur — Resolves without redirect. GitHub description: &#x27;Powerful Powerful Machine Learning library with GPU, CPU and WASM backends&#x27;.</p>

<p>Caveats: Did not run the library or test the GPU backend.; The last main-branch commit seen in the commit feed is 2024-09-30. That is informational only.</p>

</details>

<h3>written — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -143,7 +143,7 @@
 - [zerho](https://github.com/glastor-core/zerho) - High-performance documentation engine for Deno 2 and Edge runtimes with interactive playground, OpenAPI explorer, and native llms.txt support.
 
 ### String utils
-- [written](https://github.com/vixalien/written) - A provides a set of utilities for manipulating text, with a focus on providing typographic tools rather than pure string manipulation.
+- [written](https://github.com/vixalien/written) - Set of utilities for manipulating text, focused on typographic tools rather than pure string manipulation.
 
 ### Social Platform APIs
 - [discordeno](https://github.com/discordeno/discordeno) - Discord API library for Deno
```

<details>
<summary>Evidence and limitations</summary>

<p>The capabilities match the README, but the description begins &#x27;A provides a set of…&#x27;, which is ungrammatical (the contribution rules require correct grammar). The proposed wording follows the upstream text and starts with a noun phrase. It remains a Deno fork published on deno.land/x and fits String utils.</p>

<p>https://raw.githubusercontent.com/vixalien/written/master/README.md — &#x27;written provides a set of utilities for manipulating text, with a focus on providing typographic tools rather than pure string manipulation.&#x27; Deno import from https://deno.land/x/written/written.ts. Describes itself as &#x27;a Deno fork&#x27; of stephenhutchings/written.</p>

<p>https://github.com/vixalien/written — GitHub description: &#x27;A set of utilities for manipulating text, with a focus on providing typographic tools rather than pure string manipulation.&#x27;</p>

<p>Caveats: Only the grammar is corrected; the functionality was not tested.</p>

</details>

<h3>qunitx — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -159,7 +159,7 @@
 ### Testing
 - [deno-puppeteer](https://github.com/lucacasonato/deno-puppeteer) - A library which provides a high-level API to control Chromium or Chrome over the DevTools Protocol.
 - [keploy](https://github.com/keploy/keploy) - Record real traffic to generate integration tests and mock Postgres, Redis, and fetch calls.
-- [qunitx](https://github.com/izelnakri/qunitx) - Zero dependency, fully customizable, mature, universal test API that can run interchangably in node.js, Deno & browser, using default runtime test runners.
+- [qunitx](https://github.com/izelnakri/qunitx) - Zero-dependency universal test API built on QUnit that runs the same test file in Node.js, Deno and the browser.
 - [rhum](https://github.com/drashland/rhum) - A lightweight testing framework for Deno.
 - [superdeno](https://github.com/cmorten/superdeno) - Super-agent driven library for testing Deno HTTP servers.
 - [superoak](https://github.com/cmorten/superoak) - HTTP assertions for Oak made easy via SuperDeno.
```

<details>
<summary>Evidence and limitations</summary>

<p>The capabilities are confirmed: the same test file runs under node --test, deno test and a browser, with zero runtime dependencies and a JSR package. It fits Testing. The description misspells &#x27;interchangably&#x27; and styles &#x27;node.js&#x27; incorrectly, which are spelling/grammar issues under the contribution rules. The proposed wording follows the official package description.</p>

<p>https://raw.githubusercontent.com/izelnakri/qunitx/main/README.md — &#x27;One test file. Node.js, Deno, and the browser. No config.&#x27; Run with node --test, deno test, or the qunitx CLI for a real browser. &#x27;Zero runtime dependencies.&#x27; Built on QUnit&#x27;s assertion API.</p>

<p>https://raw.githubusercontent.com/izelnakri/qunitx/main/deno.json — @izelnakri/qunitx v1.4.1: &#x27;Universal test library — run the same test file in Node.js, Deno, and the browser with QUnit&#x27;s battle-tested assertion API&#x27;.</p>

<p>Caveats: Browser runs use the qunitx CLI rather than a &#x27;default runtime test runner&#x27;; the proposed wording avoids that claim.; Did not run tests.</p>

</details>

<h3>rhum — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -160,7 +160,7 @@
 - [deno-puppeteer](https://github.com/lucacasonato/deno-puppeteer) - A library which provides a high-level API to control Chromium or Chrome over the DevTools Protocol.
 - [keploy](https://github.com/keploy/keploy) - Record real traffic to generate integration tests and mock Postgres, Redis, and fetch calls.
 - [qunitx](https://github.com/izelnakri/qunitx) - Zero dependency, fully customizable, mature, universal test API that can run interchangably in node.js, Deno & browser, using default runtime test runners.
-- [rhum](https://github.com/drashland/rhum) - A lightweight testing framework for Deno.
+- [rhum](https://github.com/drashland/rhum) - Test double library providing dummies, fakes, mocks, spies and stubs.
 - [superdeno](https://github.com/cmorten/superdeno) - Super-agent driven library for testing Deno HTTP servers.
 - [superoak](https://github.com/cmorten/superoak) - HTTP assertions for Oak made easy via SuperDeno.
 - [tepi](https://deno.land/x/tepi) - A .http Test Runner
```

<details>
<summary>Evidence and limitations</summary>

<p>The description &#x27;lightweight testing framework&#x27; is outdated. Rhum v2 is officially a test double library (Dummy, Fake, Mock, Spy, Stub), not a test runner or framework. The repo is archived; that is noted but is not grounds for removal, and test doubles still fit the Testing section.</p>

<p>https://raw.githubusercontent.com/drashland/rhum/main/README.md — &#x27;Rhum is a test double library that follows test double definitions from Gerard Meszaros.&#x27; Docs at drash.land/rhum.</p>

<p>https://raw.githubusercontent.com/drashland/rhum/main/mod.ts — Exports Dummy, Fake, Mock, Spy and Stub builders. No test-runner API.</p>

<p>https://raw.githubusercontent.com/drashland/rhum/main/package.json — @drashland/rhum v2.2.0, description &#x27;A test double library&#x27;. The test:deno script runs deno test.</p>

<p>https://github.com/drashland/rhum — Repository is archived (per the packet snapshot); description &#x27;A test double library&#x27;. Last main commit 2023-01-30.</p>

<p>Caveats: Archived status is not used to judge usability. Current Deno compatibility was not tested.; Older Rhum v1 releases were a testing framework; the description follows the current default branch.</p>

</details>

<h3>buckets — remove</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -167,7 +167,6 @@
 - [unexpected](https://github.com/unexpectedjs/unexpected) - Extensible BDD assertion toolkit.
 
 ### Utils
-- [buckets](https://github.com/jacoborus/deno-buckets) - Bundle assets and scripts in a single executable file.
 - [colors](https://github.com/retraigo/colors) - Color conversions and operations in TypeScript.
 - [computed_types](https://github.com/neuledge/computed-types) - Joi like validators for Typescript and Deno.
 - [croner](https://github.com/Hexagon/croner) - Cron library with advanced scheduling features, well-documented API, and zero dependencies.
```

<details>
<summary>Evidence and limitations</summary>

<p>The author has deprecated the project. The README now contains only &#x27;# Deprecated&#x27; and a link to the Deno issue that deprecated &#x27;deno bundle&#x27;, and the GitHub description starts with &#x27;DEPRECATED&#x27;. The entry describes it as a working bundling tool, which the official repo no longer supports.</p>

<p>https://raw.githubusercontent.com/jacoborus/deno-buckets/HEAD/README.md — Full README: &#x27;# Deprecated&#x27; followed by https://github.com/denoland/deno/issues/11073.</p>

<p>https://api.github.com/repos/jacoborus/deno-buckets — Description &#x27;DEPRECATED - Bundle assets and scripts in a single executable file. Deno&#x27;, archived=false, last push 2024-03-01.</p>

<p>https://api.github.com/repos/denoland/deno/issues/11073 — Deno issue titled &#x27;Deprecate &quot;deno bundle&quot;&#x27;, closed as completed 2021-07-05. This is the underlying feature the deprecation notice points to.</p>

<p>https://raw.githubusercontent.com/jacoborus/deno-buckets/HEAD/deno.jsonc — Contains only a test task. No published package metadata suggests continued distribution.</p>

<p>Caveats: The repository is not archived, but the deprecation is stated explicitly by the author.; The author documents no successor, so replace is not applicable.</p>

</details>

<h3>tepi — remove</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -163,7 +163,6 @@
 - [rhum](https://github.com/drashland/rhum) - A lightweight testing framework for Deno.
 - [superdeno](https://github.com/cmorten/superdeno) - Super-agent driven library for testing Deno HTTP servers.
 - [superoak](https://github.com/cmorten/superoak) - HTTP assertions for Oak made easy via SuperDeno.
-- [tepi](https://deno.land/x/tepi) - A .http Test Runner
 - [unexpected](https://github.com/unexpectedjs/unexpected) - Extensible BDD assertion toolkit.
 
 ### Utils
```

<details>
<summary>Evidence and limitations</summary>

<p>The official tepi project removed Deno support. PR #14 &#x27;Rebuild on Node + termdom, publish @garndev/tepi v3.0.0&#x27; was merged 2026-10-20. Its description says the runtime is now Node-only: deno.json, mod.ts and deno.lock were removed, and JSR publishing and the publish-deno target were dropped. The current README installs only through npm, and package.json declares engines node &gt;=20.19. The listed deno.land/x/tepi is frozen at v2.0.5 from March 2026, so the catalog entry points to a Deno distribution the author no longer maintains.</p>

<p>https://github.com/jupegarnica/tepi/pull/14 — Merged 2026-10-20. &#x27;Rebuild completo de tepi sobre Node + termdom (se elimina Deno/Ink/React)&#x27;. &#x27;Runtime Node-only: fuera deno.json, mod.ts, deno.lock&#x27;. &#x27;CI/Makefile/docs actualizados (sin JSR publish, sin targets Deno)&#x27;. &#x27;publish-deno eliminado&#x27;.</p>

<p>https://raw.githubusercontent.com/jupegarnica/tepi/HEAD/package.json — name @garndev/tepi, version 3.0.1, bin tepi -&gt; bin/tepi.mjs, engines node &gt;=20.19. Scripts use tsx and vitest.</p>

<p>https://raw.githubusercontent.com/jupegarnica/tepi/HEAD/README.md — Install section now lists only &#x27;npm install -g @garndev/tepi&#x27; and npx. No Deno install instructions.</p>

<p>https://cdn.deno.land/tepi/versions/v2.0.5/meta/meta.json — The latest deno.land/x/tepi release is v2.0.5, uploaded 2026-03-21 from jupegarnica/tepi ref v2.0.5. Its README still has an &#x27;In deno&#x27; install via jsr:@garn/tepi.</p>

<p>https://jsr.io/@garn/tepi/meta.json — JSR @garn/tepi latest is 2.0.5. No v3 was published to JSR.</p>

<p>Caveats: The legacy Deno releases (deno.land/x/tepi v2.0.5 and jsr:@garn/tepi 2.0.5) are still downloadable. Their usability under current Deno was not tested.; A maintainer could instead keep the entry as a historical or legacy Deno tool. That would be an editorial choice, not a factual gap.; Earlier GitHub API calls were rate-limited, so the release metadata came from the tags feed and the PR page.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>is-kit — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -194,7 +194,7 @@
 
 ### Validation
 
-- [is-kit](https://github.com/nyaomaru/is-kit) - Build small, composable type guards with natural TypeScript narrowing and zero dependencies.
+- [is-kit](https://github.com/necoz-oss/is-kit) - Build small, composable type guards with natural TypeScript narrowing and zero dependencies.
 - [zod](https://github.com/colinhacks/zod) - TypeScript-first schema validation with static type inference.
 
 ### Web framework
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL https://github.com/nyaomaru/is-kit returns a 301 to https://github.com/necoz-oss/is-kit. JSR metadata for @nyaomaru/is-kit names the GitHub repository as owner necoz-oss, name is-kit. The project name &#x27;is-kit&#x27; is unchanged, so alphabetical ordering is unaffected. The description (composable type guards, natural narrowing, zero dependencies) matches the README and the JSR metadata, which reports Deno runtime compatibility.</p>

<p>https://github.com/nyaomaru/is-kit — HTTP 301 redirect to https://github.com/necoz-oss/is-kit.</p>

<p>https://jsr.io/api/scopes/nyaomaru/packages/is-kit — githubRepository {owner: necoz-oss, name: is-kit}; runtimeCompat.deno true; dependencyCount 0; latest 1.16.4.</p>

<p>https://raw.githubusercontent.com/necoz-oss/is-kit/main/README.md — &#x27;is-kit is a lightweight, zero-dependency toolkit for building reusable TypeScript type guards&#x27;. It composes guards while preserving TypeScript narrowing and documents a jsr:@nyaomaru/is-kit import.</p>

<p>https://raw.githubusercontent.com/necoz-oss/is-kit/main/package.json — npm name is-kit, version 1.16.4.</p>

<p>Caveats: The JSR package scope is still @nyaomaru; only the GitHub repository owner changed.</p>

</details>

<h3>faster — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -202,7 +202,7 @@
 - [aqua](https://github.com/predetermined/aqua) - A minimal and fast web framework for Deno.
 - [danet](https://github.com/Savory/Danet) - A Savory web framework for Deno heavily inspired by [Nest.js](https://nestjs.com).
 - [drash](https://github.com/drashland/drash) - A REST microframework for Deno's HTTP server with zero dependencies.
-- [faster](https://github.com/hviana/faster) - A fast and optimized middleware server with a set of useful middlwares.
+- [faster](https://github.com/hviana/faster) - A fast and optimized middleware server with a set of useful middlewares.
 - [faster_react](https://github.com/hviana/faster_react) - Full Stack web framework with React + Faster. Fully compatible with Deno Deploy.
 - [hono](https://github.com/honojs/hono) - Ultrafast web framework for Cloudflare Workers, Deno, and Bun. Fast, but not only fast.
 - [oak](https://github.com/oakserver/oak) - A middleware framework for Deno's net server.
```

<details>
<summary>Evidence and limitations</summary>

<p>The description is accurate: the README calls Faster a &#x27;fast and optimized middleware server&#x27; with no dependencies and a collection of useful middlewares (log, static, CORS, session, rate limit, etc.). However, the catalog text misspells &#x27;middlwares&#x27;. The contribution rules require correct spelling, so the proposed update only fixes the typo.</p>

<p>https://raw.githubusercontent.com/hviana/faster/master/README.md — &#x27;Faster is a fast and optimized middleware server with an incredibly small codebase (~300 lines), built on top of native HTTP APIs with no dependencies. It includes a collection of useful middlewares (Some are specific to Deno).&#x27; Fully compatible with Deno Deploy.</p>

<p>https://raw.githubusercontent.com/hviana/faster/master/deno.json — name @hviana/faster, version 1.1.2.</p>

<p>Caveats: This is a spelling fix, not a change in project status.; The code was not run.</p>

</details>

<h3>faster_react — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -203,7 +203,7 @@
 - [danet](https://github.com/Savory/Danet) - A Savory web framework for Deno heavily inspired by [Nest.js](https://nestjs.com).
 - [drash](https://github.com/drashland/drash) - A REST microframework for Deno's HTTP server with zero dependencies.
 - [faster](https://github.com/hviana/faster) - A fast and optimized middleware server with a set of useful middlwares.
-- [faster_react](https://github.com/hviana/faster_react) - Full Stack web framework with React + Faster. Fully compatible with Deno Deploy.
+- [faster_react](https://github.com/hviana/faster_react) - Full Stack web framework with React + Faster.
 - [hono](https://github.com/honojs/hono) - Ultrafast web framework for Cloudflare Workers, Deno, and Bun. Fast, but not only fast.
 - [oak](https://github.com/oakserver/oak) - A middleware framework for Deno's net server.
   - [oak-http-proxy](https://github.com/cmorten/oak-http-proxy) - Proxy middleware for Deno Oak HTTP servers.
```

<details>
<summary>Evidence and limitations</summary>

<p>faster_react is still a Deno full-stack React framework built on Faster (deno.json imports jsr:@hviana/faster). But the README now opens with a warning: &#x27;Serverless functionality is temporarily unavailable due to recent changes to the Deno.bundle API.&#x27; That contradicts the catalog&#x27;s unqualified &#x27;Fully compatible with Deno Deploy.&#x27; The suggested update drops that volatile claim and keeps the durable description.</p>

<p>https://raw.githubusercontent.com/hviana/faster_react/main/README.md — Warning banner: &#x27;Please note: Serverless functionality is temporarily unavailable due to recent changes to the Deno.bundle API. This will be fixed as soon as the Deno API allows it.&#x27; Introduction: &#x27;faster_react is a tiny Full-Stack React framework&#x27;. Features include &#x27;Automatic detection of Deno Deploy environment&#x27;.</p>

<p>https://raw.githubusercontent.com/hviana/faster_react/main/deno.json — name @faster/react; imports faster from jsr:@hviana/faster@1.1.2 and faster_react_core from deno.land/x.</p>

<p>Caveats: The GitHub repo description still claims full Deno Deploy/serverless compatibility, which conflicts with the README warning. The README warning is more specific and current.; The breakage is described as temporary; the shorter wording stays accurate either way.; Deno Deploy was not tested.</p>

</details>

<h3>fresh_chart — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -219,7 +219,7 @@
 ### Web utils
 - [djwt](https://github.com/Zaubrik/djwt) - Make JSON Web Tokens (JWT) on Deno based on JWT and JWS specifications.
 - [forwarded](https://github.com/deno-libs/forwarded) - Deno port of `forwarded` library.
-- [fresh_chart](https://github.com/denoland/fresh_charts) - A server-side-rendered charting library for Fresh.
+- [fresh_charts](https://github.com/denoland/fresh_charts) - A server-side-rendered charting library for Fresh.
 - [gentleRpc](https://github.com/timonson/gentle_rpc) - A JSON-RPC 2.0 TypeScript library for Deno and the browser.
 - [gql](https://github.com/deno-libs/gql) - Universal GraphQL HTTP middleware.
 - [graphql-tag](https://github.com/deno-libs/graphql_tag) - GraphQL schema AST from template literal.
```

<details>
<summary>Evidence and limitations</summary>

<p>Identity fix: the entry is named &quot;fresh_chart&quot;, but the canonical repository and README title are &quot;fresh_charts&quot; (denoland/fresh_charts). The description stays accurate: the README documents server-side rendering via the Chart component and renderChart(). It also mentions client-side islands, but that is an addition, not a correction. The repo is archived, which I note as a status caveat. The README gives no deprecation notice or successor. The demo site fresh-charts.deno.dev returned 502 at check time. Renaming keeps alphabetical order (forwarded &lt; fresh_charts &lt; gentleRpc).</p>

<p>https://api.github.com/repos/denoland/fresh_charts — full_name denoland/fresh_charts, archived=true, last pushed 2024-04-17, description &quot;A server-side-rendered charting library for Fresh&quot;.</p>

<p>https://raw.githubusercontent.com/denoland/fresh_charts/main/README.md — Title &quot;# fresh_charts&quot;. &quot;A charting library for Fresh based on Chart.js, which supports server and client side rendering.&quot; It gives no successor or deprecation statement.</p>

<p>https://raw.githubusercontent.com/denoland/fresh_charts/main/deno.json — Imports pin $fresh to deno.land/x/fresh@1.4.2, so it targets Fresh 1.x.</p>

<p>https://fresh-charts.deno.dev/ — Returned HTTP 502 at check time. This may be temporary, so recheck.</p>

<p>Caveats: The repo is archived and pinned to Fresh 1.x. I did not test compatibility with current Fresh. Archival alone is not grounds for removal.; The demo site was down (502) when checked.</p>

</details>

<h3>gentleRpc — replace</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The gentle_rpc README states: &quot;The gentle_rpc library is no longer maintained. Please switch to our new and improved RPC library, schicksal&quot; and links Zaubrik/schicksal. That makes schicksal an officially documented successor. Zaubrik/schicksal exists and is not archived. It describes itself as a &quot;JSON-RPC 2.0 library for deno and the browser&quot;, so the current description still fits. However, renaming to &quot;schicksal&quot; while keeping the entry between fresh_chart and gql would break alphabetical order. The entry would have to move after rpc in the Web utils section.</p>

<p>https://raw.githubusercontent.com/timonson/gentle_rpc/master/README.md — &quot;Important Notice: The gentle_rpc library is no longer maintained. Please switch to our new and improved RPC library, schicksal, available at schicksal on GitHub (https://github.com/Zaubrik/schicksal).&quot;</p>

<p>https://api.github.com/repos/Zaubrik/schicksal — full_name Zaubrik/schicksal, archived=false, last pushed 2024-05-22, description &quot;JSON-RPC 2.0 library for deno and the browser&quot;.</p>

<p>https://raw.githubusercontent.com/Zaubrik/schicksal/main/README.md — &quot;JSON-RPC 2.0 library based on ES modules.&quot; It shows client makeRpcCall and makeBatchRpcCall usage.</p>

<p>Blocking questions: Ordering: under deterministic in-place replacement, &quot;schicksal&quot; would sit between forwarded/fresh_chart and gql, which violates the alphabetical rule for the Web utils section. The entry must be moved after rpc (or wherever alphabetical order requires).</p>

<p>Caveats: I did not verify whether schicksal supports WebSockets like gentle_rpc did. The proposed description does not claim it.; schicksal&#x27;s last push was 2024-05.</p>

</details>

<h3>nats — replace</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -223,7 +223,7 @@
 - [gentleRpc](https://github.com/timonson/gentle_rpc) - A JSON-RPC 2.0 TypeScript library for Deno and the browser.
 - [gql](https://github.com/deno-libs/gql) - Universal GraphQL HTTP middleware.
 - [graphql-tag](https://github.com/deno-libs/graphql_tag) - GraphQL schema AST from template literal.
-- [nats](https://github.com/nats-io/nats.deno) - A Deno client for the [NATS messaging system](https://nats.io/).
+- [nats](https://github.com/nats-io/nats.js) - A Deno client for the [NATS messaging system](https://nats.io/).
 - [obsidian](https://github.com/open-source-labs/obsidian) - A native GraphQL caching client and server module.
 - [router](https://github.com/zhmushan/router) - A high-performance basic router works anywhere.
 - [rpc](https://github.com/deno-libs/rpc) - JSONRPC server implementation for Deno.
```

<details>
<summary>Evidence and limitations</summary>

<p>The nats.deno README officially states &quot;Nats.deno is now part of nats.js&quot; and links a migration guide. The nats.js README says it &quot;now supersedes nats.deno&quot; and hosts a Deno transport (@nats-io/transport-deno on JSR). nats.js is an officially documented successor from the same org. The description &quot;A Deno client for the NATS messaging system&quot; stays accurate for nats.js&#x27;s Deno transport. The name &quot;nats&quot; can be kept, so there is no ordering impact. The entry has an inline nats.io link, so only the primary URL changes.</p>

<p>https://raw.githubusercontent.com/nats-io/nats.deno/main/README.md — &quot;[!IMPORTANT] Nats.deno is now part of nats.js (https://github.com/nats-io/nats.js). Changes are well documented... described in migration.md.&quot;</p>

<p>https://raw.githubusercontent.com/nats-io/nats.js/main/README.md — &quot;This repository now supersedes: nats.deno, nats.ws...&quot; It hosts native transports for Deno, Node/Bun and browsers. Beginning with v3 it is a mono-repo.</p>

<p>https://raw.githubusercontent.com/nats-io/nats.js/main/transport-deno/README.md — &quot;NATS Deno Transport - A NATS client for Deno&quot;. Install via jsr:@nats-io/transport-deno.</p>

<p>https://api.github.com/repos/nats-io/nats.js — archived=false, last pushed 2026-11-10, description &quot;JavaScript client for Node.js, Bun, Deno and browser for NATS&quot;.</p>

<p>Caveats: The maintainer may prefer linking the transport-deno subdirectory rather than the repo root. The contribution rules say to link the GitHub repo, so the root is proposed.; nats.deno itself is not archived. Its existing deno.land/x releases remain available.</p>

</details>

<h3>deno.land/x/ — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -237,7 +237,7 @@
 
 ## Registries
 
-- [deno.land/x/](https://deno.land/x/) - The official 3rd party module registry.
+- [deno.land/x/](https://deno.land/x/) - The official, now read-only, third-party module hosting service.
 - [nest.land](https://nest.land) - An immutable, blockchain powered Deno package registry. 🥚
 
 ## Showcases
```

<details>
<summary>Evidence and limitations</summary>

<p>The deno.land/x page now states &quot;deno.land/x is now read-only. Existing modules and versions remain available and immutable, but no new modules or versions can be published here. New packages should be published to JSR.&quot; It still officially hosts existing third-party modules, so it remains relevant to the Registries section. But &quot;The official 3rd party module registry&quot; no longer accurately describes its role, since it is read-only and new publishing has moved to JSR. A dated clarification is warranted. JSR is not proposed as a replacement because deno.land/x still serves existing modules.</p>

<p>https://deno.land/x — Page text: &quot;deno.land/x is now read-only. Existing modules and versions remain available, but new modules and versions can no longer be published here. Publish new packages to JSR, the modern registry for Deno and the broader JavaScript ecosystem.&quot; It also says &quot;deno.land/x is a hosting service for Deno scripts.&quot; It lists 7741 modules.</p>

<p>Caveats: The maintainer may separately consider whether JSR should be listed in Registries. That is outside this entry.</p>

</details>

<h3>deno_docker — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -263,7 +263,7 @@
 - [denopendabot](https://github.com/apps/denopendabot) - Dependabot for Deno projects.
 - [denopkg](https://github.com/egoist-labs/denopkg.com) - An easier way to use code from GitHub in your Deno project.
 - [Deno Dig](https://github.com/theGEBIRGE/DenoDig) - A tool for extracting application code and npm packages from stand-alone Deno executables.
-- [deno_docker](https://github.com/denoland/deno_docker) - Latest dockerfiles and images for Deno - alpine, centos, debian, ubuntu.
+- [deno_docker](https://github.com/denoland/deno_docker) - Official Dockerfiles and images for Deno - Alpine, Debian, Distroless and Ubuntu.
 - [dmm](https://github.com/drashland/dmm) - Lightweight Deno Module Manager
 - [dnt](https://github.com/denoland/dnt) - Deno to npm package build tool.
 - [dpm](https://github.com/dpmland/dpm) - Deno Package Manager, a NPM | Yarn Experience for Deno
```

<details>
<summary>Evidence and limitations</summary>

<p>denoland/deno_docker is canonical and active, but the entry&#x27;s distro list is outdated. The README lists Alpine, Debian (default), Distroless, Ubuntu and a binary-only image. The repo root has alpine/bin/debian/distroless/ubuntu dockerfiles and no CentOS dockerfile. The listed &#x27;centos&#x27; variant is no longer provided; the GitHub repo description is also stale.</p>

<p>https://github.com/denoland/deno_docker — README: &#x27;Alpine Linux: denoland/deno:alpine; Debian: denoland/deno:debian (default); Distroless: denoland/deno:distroless; Ubuntu: denoland/deno:ubuntu; Only the binary: denoland/deno:bin&#x27;; published on Docker Hub and GHCR.</p>

<p>https://api.github.com/repos/denoland/deno_docker/contents/ — Root files: alpine.dockerfile, bin.dockerfile, debian.dockerfile, distroless.dockerfile, ubuntu.dockerfile; no centos dockerfile.</p>

<p>https://api.github.com/repos/denoland/deno_docker — archived=false, pushed_at 2026-10-21; repo description still says &#x27;alpine, centos, debian, ubuntu&#x27; (stale relative to README/files).</p>

<p>Caveats: Image variants may change again; a shorter wording without the distro list would be more durable.</p>

</details>

<h3>axetroy/dvm — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -270,7 +270,7 @@
 - dvm
   - [asdf-community/asdf-deno](https://github.com/asdf-community/asdf-deno) - Deno plugin for [asdf](https://asdf-vm.com/)
   - [justjavac/dvm](https://github.com/justjavac/dvm) - Deno Version Manager: manage multiple active Deno versions.
-  - [axetroy/dvm](https://github.com/axetroy/dvm) - Version manger for Deno without runtime dependencies.
+  - [axetroy/dvm](https://github.com/axetroy/dvm) - Version manager for Deno without runtime dependencies.
   - [ghosind/dvm](https://github.com/ghosind/dvm) - A lightweight Deno Version Manager for Linux/MacOS.
 - [entype](https://github.com/bcheidemann/entype) - A CLI tool used to generate type definitions for serialised data, currently supporting JSON to Rust and TypeScript.
 - [kopo-cli](https://github.com/littletof/kopo-cli) - A Deno registry browser in the terminal.
```

<details>
<summary>Evidence and limitations</summary>

<p>The project is relevant and correctly described: a Deno version manager with no runtime dependencies. The entry misspells &#x27;manager&#x27; as &#x27;manger&#x27;. This is a spelling correction under the contribution rules (&#x27;Check your spelling and grammar&#x27;).</p>

<p>https://github.com/axetroy/dvm — Returned HTTP 200 with no redirect. Snapshot: not archived; Go module (go.mod); description &#x27;🚀 Fast and simple version manger for Deno without runtime dependencies&#x27;. The upstream text carries the same typo.</p>

<p>https://raw.githubusercontent.com/axetroy/dvm/master/README.md — &#x27;dvm is a command-line tool to manage Deno versions.&#x27; Features include &#x27;No runtime dependencies&#x27; and cross-platform support. Commands include install, use, ls-remote and exec.</p>

<p>Caveats: This is a spelling-only correction; no factual mismatch was found. The tool was not run.</p>

</details>

<h3>vscode-deno — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -280,7 +280,7 @@
 - [studio-pack-generator](https://github.com/jersou/studio-pack-generator) - Convert a folder or a RSS URL to Studio pack for Lunii device
 - [trex](https://github.com/crewdevio/Trex) - Package management like npm for deno.
 - [udd](https://github.com/hayd/deno-udd) - Update Deno dependencies: updates import statements to their latest published version.
-- [vscode-deno](https://github.com/denoland/vscode_deno) - VS Code extension that provides Deno support using the `TypeScript Deno language service plugin`.
+- [vscode-deno](https://github.com/denoland/vscode_deno) - VS Code extension that provides Deno support, powered by the Deno language server. `TypeScript Deno language service plugin`.
 
 ## Integrations
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The entry says the extension provides Deno support &#x27;using the TypeScript Deno language service plugin&#x27;. The current README says it is &#x27;powered by the Deno language server&#x27;. The bundled typescript-deno-plugin&#x27;s README says its main purpose is to disable parts of VS Code&#x27;s built-in TS server, with language information coming from the Deno CLI language server. The &#x27;using ...&#x27; claim is therefore outdated. The name, URL and relevance are correct.</p>

<p>https://github.com/denoland/vscode_deno — Returned HTTP 200 with no redirect. Snapshot: not archived; description &#x27;Visual Studio Code plugin for Deno&#x27;.</p>

<p>https://raw.githubusercontent.com/denoland/vscode_deno/main/README.md — &#x27;This extension adds support for using Deno with Visual Studio Code, powered by the Deno language server.&#x27; It requires the Deno CLI v1.13.0 or later.</p>

<p>https://raw.githubusercontent.com/denoland/vscode_deno/main/typescript-deno-plugin/README.md — &#x27;The main purpose of the plugin is to disable parts of the built in TypeScript/JavaScript language server ... as language server information will be obtained from the Deno CLI Language Server itself.&#x27;</p>

<p>Caveats: The current line ends with an inline code span (`TypeScript Deno language service plugin`) that the parser treats as a suffix. The applied edit must replace the whole description, including that span.</p>

</details>

<h3>Netlify Edge Functions — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -284,7 +284,7 @@
 
 ## Integrations
 
-- [Netlify Edge Functions](https://docs.netlify.com/edge-functions/overview/) - Edge Functions connect the Netlify platform and workflow.
+- [Netlify Edge Functions](https://docs.netlify.com/build/edge-functions/overview/) - Edge Functions connect the Netlify platform and workflow.
 - [Slack Custom Functions](https://api.slack.com/future/functions/custom) - Build custom Run On Slack functions using Deno.
 - [Smallweb](https://www.smallweb.run/) - A personal cloud contained in a single directory. You can customize the server behavior using Deno.
 - [Supabase Edge Functions](https://supabase.com/docs/guides/functions) - Edge Functions are server-side TypeScript functions, distributed globally at the edge.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL redirects to https://docs.netlify.com/build/edge-functions/overview/. The page still opens with &#x27;Edge Functions connect the Netlify platform and workflow ...&#x27; and states the runtime is based on Deno, so the description and fit are supported. Only the URL needs updating to the canonical location.</p>

<p>https://docs.netlify.com/edge-functions/overview/ — Resolves (HTTP 200) to https://docs.netlify.com/build/edge-functions/overview/.</p>

<p>https://docs.netlify.com/build/edge-functions/overview.md — &#x27;Edge Functions connect the Netlify platform and workflow with an open runtime standard at the network edge.&#x27; Also: &#x27;All this dynamic processing happens in a secure runtime based on Deno&#x27;.</p>

<p>Caveats: The old URL still redirects, so the update is not urgent.</p>

</details>

<h3>Slack Custom Functions — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -285,7 +285,7 @@
 ## Integrations
 
 - [Netlify Edge Functions](https://docs.netlify.com/edge-functions/overview/) - Edge Functions connect the Netlify platform and workflow.
-- [Slack Custom Functions](https://api.slack.com/future/functions/custom) - Build custom Run On Slack functions using Deno.
+- [Slack Custom Functions](https://docs.slack.dev/tools/deno-slack-sdk/guides/creating-custom-functions/) - Build custom Run On Slack functions using Deno.
 - [Smallweb](https://www.smallweb.run/) - A personal cloud contained in a single directory. You can customize the server behavior using Deno.
 - [Supabase Edge Functions](https://supabase.com/docs/guides/functions) - Edge Functions are server-side TypeScript functions, distributed globally at the edge.
 - [Astro](https://docs.astro.build/en/guides/deploy/deno/) - Deploy a server-side rendered Astro site to Deno Deploy.
```

<details>
<summary>Evidence and limitations</summary>

<p>api.slack.com/future/functions/custom redirects to the Deno Slack SDK guide &#x27;Creating custom functions&#x27; on docs.slack.dev. The page documents defining custom workflow functions with DefineFunction in the Deno Slack SDK, so the entry is relevant. Update the URL to the canonical docs.slack.dev page.</p>

<p>https://api.slack.com/future/functions/custom — Resolves (HTTP 200) to https://docs.slack.dev/tools/deno-slack-sdk/guides/creating-custom-functions/.</p>

<p>https://docs.slack.dev/tools/deno-slack-sdk/guides/creating-custom-functions/ — Page titled &#x27;Creating custom functions&#x27; under Deno Slack SDK. &#x27;Custom functions are how you define custom workflow steps&#x27;, defined via DefineFunction. A &#x27;Deno &amp; TypeScript&#x27; section sits in the same SDK nav.</p>

<p>https://docs.slack.dev/tools/deno-slack-sdk/ — &#x27;You can create Slack-hosted workflows written in TypeScript using the Deno Slack SDK.&#x27;</p>

<p>Caveats: The fetched pages never use the phrase &#x27;Run On Slack&#x27;; current docs say &#x27;Slack-hosted&#x27;. The maintainer may optionally reword to current terminology, for example &#x27;Build custom workflow functions for Slack-hosted apps using the Deno Slack SDK.&#x27; The existing wording is dated branding, not clearly false.; Workflow apps require a paid Slack plan, per the docs.</p>

</details>

<h3>Building API&#x27;s using Deno, Oak and MYSQL — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The URL now serves a different article. It is titled &#x27;Build a Deno API Server with MySQL&#x27;, published 2026-08-28 and modified 2026-09-29. It uses a plain HTTP handler with npm:mysql2 and never mentions Oak, so the catalog name &#x27;Building API&#x27;s using Deno, Oak and MYSQL&#x27; no longer describes the page. The page is still relevant to Deno. Proposed edit: change the name to the current title.</p>

<p>https://codeforgeek.com/building-api-server-using-deno-and-mysql/ — HTTP 200, no redirect. h1 &#x27;Build a Deno API Server with MySQL&#x27;; datePublished 2026-08-28, dateModified 2026-09-29. Sections: &#x27;Install Deno and prepare MySQL&#x27;, &#x27;Build the HTTP handler&#x27;, &#x27;Connect the handler to MySQL2&#x27;, &#x27;Run the handler checks&#x27;, &#x27;Set a production boundary&#x27;. &#x27;Oak&#x27; appears 0 times; &#x27;npm:mysql2/promise&#x27; appears twice.</p>

<p>Blocking questions: Articles is ordered chronologically. The page is now a 2026 article sitting among 2020 entries, so renaming it in place may break the ordering rule. The maintainer must decide whether to move it, keep it, or point to an archived copy of the original Oak article.</p>

<p>Caveats: I did not retrieve an archived copy of the original Oak-based article to compare.; The page is a rewrite by the same publisher at the same URL.</p>

</details>

<h3>Continuous Integration with Deno — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -307,7 +307,7 @@
 - [Create a simple Note-taking app with Deno](https://dev.to/jeferson_sb/create-a-simple-note-taking-app-with-deno-3k7g)
 - [Building API's using Deno, Oak and MYSQL](https://codeforgeek.com/building-api-server-using-deno-and-mysql/)
 - [Create your first News CLI app using Deno](https://medium.com/javascript-in-plain-english/creating-your-first-news-cli-app-using-deno-e1470398c627)
-- [Continuous Integration with Deno](https://semaphoreci.com/blog/continuous-integration-with-deno)
+- [Continuous Integration with Deno](https://semaphore.io/blog/continuous-integration-with-deno)
 - [The Hidden Superpower of Deno: xeval](https://stefanbuck.com/blog/hidden-superpower-deno-xeval)
 - Deno REST API with Oak Tutorial Series [0](https://www.robinwieruch.de/deno-tutorial), [1](https://www.robinwieruch.de/deno-oak), [2](https://www.robinwieruch.de/deno-oak-rest-api)
 - [Getting Started with Deno](https://sabe.io/tutorials/getting-started-with-deno)
```

<details>
<summary>Evidence and limitations</summary>

<p>The article is live and its title matches. It is from June 2020 and covers CI for Deno projects. semaphoreci.com now redirects to semaphore.io, so the proposed edit is a URL update to the canonical domain.</p>

<p>https://semaphoreci.com/blog/continuous-integration-with-deno — Redirects to https://semaphore.io/blog/continuous-integration-with-deno (HTTP 200).</p>

<p>https://semaphore.io/blog/continuous-integration-with-deno — Title &#x27;Continuous Integration with Deno - Semaphore&#x27;, published 2020-06-30. The content mentions &#x27;deno test&#x27; and Semaphore.</p>

<p>Caveats: The old URL still works through the redirect, so the update is optional.</p>

</details>

<h3>Slides — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -319,7 +319,7 @@
   - [Slides](https://tinyclouds.org/jsconf2018.pdf)
 - [JSDC 2018#A01 - Deno, A New Server-Side Runtime By Ryan Dahl](https://www.youtube.com/watch?v=FlTG0UXRAkE)
 - [Ryan Dahl. Deno, a new way to JavaScript. JS Fest 2019 Spring](https://www.youtube.com/watch?v=z6JRlx5NC9E)
-  - [Slides](https://www.slideshare.net/JSFestUA/js-fest-2019-ryan-dahl-deno-a-new-way-to-javascript)
+  - [Slides](https://www.slideshare.net/slideshow/js-fest-2019-ryan-dahl-deno-a-new-way-to-javascript/140049045)
 - [Rafał Pocztarski — From Node.js to Deno - JavaScript/TypeScript runtime built with V8 and Rust [EN]](https://www.youtube.com/watch?v=Aib1OZLy0_c)
 - [Ryan Dahl: A secure runtime for JavaScript and TypeScript | js.la April 2019](https://www.youtube.com/watch?v=RAmqgbv247s)
   - [Slides](https://docs.google.com/presentation/d/1CSQVTeH5tFzE4AZVXIpx9Xwew5YS-gxJZ03eRFtNeIc/edit)
```

<details>
<summary>Evidence and limitations</summary>

<p>The legacy SlideShare URL returns HTTP 200 after redirecting to the canonical /slideshow/ URL. That page holds the matching JS Fest 2019 Ryan Dahl deck. The only change is the canonical URL. The current link still works through the redirect, so this update is optional.</p>

<p>https://www.slideshare.net/slideshow/js-fest-2019-ryan-dahl-deno-a-new-way-to-javascript/140049045 — The legacy URL redirects here. Page title and og:title: &#x27;JS Fest 2019. Ryan Dahl. Deno, a new way to JavaScript&#x27;.</p>

<p>Caveats: The redirect still works, so leaving the link as it is also acceptable.</p>

</details>

<h3>Deno 并不是下一代 Node.js — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -344,7 +344,7 @@
 
 ### Chinese
 
-- [Deno 并不是下一代 Node.js](https://juejin.im/post/5b14a390e51d4506c1300bbc)
+- [Deno 并不是下一代 Node.js](https://juejin.cn/post/6844903616143179784)
 - [玩 Deno 遇到问题的解决方案](https://juejin.im/post/5b1245b3f265da6e4c6cf249)
 - [让我们一起来学习别人学不动的 Deno](https://segmentfault.com/a/1190000015151287)
 - [Design Mistakes in Node zh-CN](https://zhuanlan.zhihu.com/p/37637923)
```

<details>
<summary>Evidence and limitations</summary>

<p>The legacy juejin.im URL returns HTTP 200 after redirecting to juejin.cn/post/6844903616143179784, which is Juejin&#x27;s current domain and ID scheme. The article is justjavac&#x27;s 2018-06-04 essay on early Deno, a dated Chinese resource that fits the section. The only change is the canonical URL.</p>

<p>https://juejin.cn/post/6844903616143179784 — The listed juejin.im URL redirects here with HTTP 200. The page served only a JS &#x27;Please wait...&#x27; challenge to curl and WebFetch, so I could not read the article body.</p>

<p>https://segmentfault.com/a/1190000015159728 — A search result points to a SegmentFault copy of &#x27;Deno 并不是下一代 Node.js&#x27;. The search summary attributes it to justjavac, 2018-06-04. I did not open this page myself.</p>

<p>Caveats: The article&#x27;s technical content (the Go-based prototype) is historical. That is expected for a dated 2018 article.; The redirect is enough reason to update the URL, but I did not see the article text on Juejin.</p>

</details>

<h3>玩 Deno 遇到问题的解决方案 — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -345,7 +345,7 @@
 ### Chinese
 
 - [Deno 并不是下一代 Node.js](https://juejin.im/post/5b14a390e51d4506c1300bbc)
-- [玩 Deno 遇到问题的解决方案](https://juejin.im/post/5b1245b3f265da6e4c6cf249)
+- [玩 Deno 遇到问题的解决方案](https://juejin.cn/post/6844903615669207053)
 - [让我们一起来学习别人学不动的 Deno](https://segmentfault.com/a/1190000015151287)
 - [Design Mistakes in Node zh-CN](https://zhuanlan.zhihu.com/p/37637923)
 - [Node之父ry：Node中的设计错误](https://mp.weixin.qq.com/s/7XAiYw18c8YZc-fXk0-wrw)
```

<details>
<summary>Evidence and limitations</summary>

<p>The legacy juejin.im URL returns HTTP 200 after redirecting to juejin.cn/post/6844903615669207053. According to search results, a third-party Chinese Deno index lists the article as published 2018-06-02. The only change is the canonical URL.</p>

<p>https://juejin.cn/post/6844903615669207053 — The listed juejin.im URL redirects here with HTTP 200. The page served only a JS &#x27;Please wait...&#x27; challenge, so I could not read the title or body.</p>

<p>https://hylerrix.github.io/awesome-deno-cn/ — According to the search results, this index lists &#x27;玩 Deno 遇到问题的解决方案&#x27; as published 2018-06-02. I did not open this page myself.</p>

<p>Caveats: I could not render the article text on Juejin. The identity rests on Juejin&#x27;s own redirect.</p>

</details>

<h3>Deno - L&#x27;anagramma di Node — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -363,7 +363,7 @@
 
 ### Italian
 
-- [Deno - L'anagramma di Node](https://www.slideshare.net/FrancescoSciuti/deno-lanagramma-di-node)
+- [Deno - L'anagramma di Node](https://www.slideshare.net/slideshow/deno-lanagramma-di-node/235465264)
 
 ### Japanese
 
```

<details>
<summary>Evidence and limitations</summary>

<p>Francesco Sciuti&#x27;s Italian Deno slides are live and still fit the Italian section. However, the listed SlideShare URL now permanently redirects (301) to the /slideshow/ URL, so the link should be updated to the canonical form.</p>

<p>https://www.slideshare.net/FrancescoSciuti/deno-lanagramma-di-node — Returns HTTP 301 to https://www.slideshare.net/slideshow/deno-lanagramma-di-node/235465264.</p>

<p>https://www.slideshare.net/slideshow/deno-lanagramma-di-node/235465264 — HTTP 200. Title &#x27;Deno - L&#x27;anagramma di node&#x27;, author Francesco Sciuti, datePublished 2020-06-12. The description (Italian) presents Deno, Ryan Dahl&#x27;s new JavaScript runtime, and its differences from Node.</p>

<p>Caveats: The old URL still works through the redirect, so this update is optional.</p>

</details>

<h3>A short introduction to Deno — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -390,4 +390,4 @@
 
 ### Kurdish (Central)
 
-- [A short introduction to Deno](https://devs.krd/about-deno)
+- [A short introduction to Deno](https://devs.krd/deno-introduction/)
```

<details>
<summary>Evidence and limitations</summary>

<p>The Kurdish (Central) Deno introduction is live and fits the section. The listed URL permanently redirects (301) to a new path, so the link should be updated to the canonical URL.</p>

<p>https://devs.krd/about-deno — Returns HTTP 301 with Location https://devs.krd/deno-introduction/.</p>

<p>https://devs.krd/deno-introduction/ — HTTP 200, title &#x27;گەشەپێدەرانی کورد | کورتەیەک لەسەر دینۆ&#x27; (&#x27;Kurdish developers | a short note about Deno&#x27;). The description (Central Kurdish) introduces Deno as a modern, secure TypeScript/JavaScript runtime made by Node.js creator Ryan Dahl.</p>

<p>Caveats: The old URL still works through the redirect.</p>

</details>

## Uncertain findings

<h3>cac — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>cac is still active and the description is still its own tagline. However, the current v7 line seems to have dropped Deno support. v6.7.14 had a README section &#x27;With Deno&#x27; (importing https://unpkg.com/cac/mod.ts) and a mod.ts file. On main, mod.ts returns 404, the README no longer mentions Deno, and package.json only declares a Node engine. The v7.0.0 notes list ESM-only and Node &gt;= 20.19 changes but say nothing explicit about Deno.</p>

<p>https://raw.githubusercontent.com/cacjs/cac/main/package.json — v7.1.0. The description is &#x27;Simple yet powerful framework for building command-line apps.&#x27; It declares engines node &gt;=20.19.0 and nothing Deno-specific.</p>

<p>https://raw.githubusercontent.com/cacjs/cac/v6.7.14/README.md — The v6 README has a &#x27;With Deno&#x27; section: import { cac } from &#x27;https://unpkg.com/cac/mod.ts&#x27;.</p>

<p>https://raw.githubusercontent.com/cacjs/cac/main/README.md — The current README does not mention Deno. Install instructions are only &#x27;npm i cac&#x27;. On main, mod.ts returns 404 (it returns 200 at tag v6.7.14).</p>

<p>https://github.com/cacjs/cac/releases/tag/v7.0.0 — Breaking changes: drop Node &lt; 20.19, remove the CJS build (ESM-only), rename the event listener methods. The page does not mention Deno.</p>

<p>Blocking questions: Unresolved: whether cac still officially supports or targets Deno now that the Deno entrypoint and docs are gone, and whether the maintainer counts npm-only packages as in scope for CLI utils.</p>

<p>Caveats: Deno was not run, so it is untested whether &#x27;npm:cac&#x27; v7 works in Deno.; Releases could not be listed through the GitHub API because of rate limiting.</p>

</details>

<h3>lume — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>Lume&#x27;s identity and description are still accurate (an SSG inspired by Jekyll/Eleventy with multiple file formats). Its Deno relevance is now ambiguous. The official site and README say Lume 4.0 &#x27;has been released and ported to Node&#x27; and requires Node v24. The main-branch README calls it a generator &#x27;for Node&#x27; and says &#x27;Previous Lume versions were available for Deno&#x27;. Lume 3 (Deno) lives on a v3 branch with a commit as recent as 2026-10-20, but no official support policy for it was found. Two options for the maintainer: keep it with a note such as &#x27;Lume 3 and earlier run on Deno; Lume 4 runs on Node&#x27;, or remove it.</p>

<p>https://raw.githubusercontent.com/lumeland/lume/main/README.md — &#x27;a (yet another) static site generator for Node. Previous Lume versions were available for Deno.&#x27; Quick start uses &#x27;npx @lumeland/lume build&#x27;.</p>

<p>https://lume.land/docs/overview/installation/ — Site banner: &#x27;Lume 4.0 has been released and ported to Node.&#x27; Prerequisites: &#x27;Lume requires Node v24 LTS or newer&#x27;. Setup uses &#x27;npm create lume@latest&#x27;.</p>

<p>https://lume.land/blog/posts/lume-4/ — Author post (Nov 4, 2026) explains porting Lume to Node as Lume 4. It shows the Lume 3 (Deno) vs Lume 4 (Node) config, says JSR dependencies were removed, and says porting to other runtimes may be explored later. It also claims Deno is &#x27;sunsetting&#x27;; that claim was not independently verified.</p>

<p>https://raw.githubusercontent.com/lumeland/lume/v3/README.md — v3 branch README: &#x27;static site generator for Deno&#x27;. The branch commit feed shows an update on 2026-10-20.</p>

<p>https://raw.githubusercontent.com/lumeland/lume/main/packages/lume/package.json — @lumeland/lume v4.0.2 is an npm workspace package (pnpm monorepo), not a Deno module.</p>

<p>Blocking questions: Relevance is ambiguous: the current major version officially targets Node, while Lume 3 for Deno remains on a v3 branch with no published support or end-of-life policy.; Unresolved: whether a dated or version-qualified description (Lume 3 on Deno) is acceptable under the list&#x27;s conventions, or whether the maintainer prefers removal.</p>

<p>Caveats: Did not test whether Lume 4 runs on Deno through npm compatibility; the official docs only document Node.; The Lume blog&#x27;s claim about Deno&#x27;s future is untrusted third-party context and was not used as evidence for other entries.</p>

</details>

<h3>keploy — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The description is broadly accurate: Keploy records real API traffic to generate tests and mocks for databases including Postgres and Redis, plus outbound HTTP calls. Deno relevance is unconfirmed. Keploy is a Go, eBPF-based tool that claims to work with &#x27;any language, framework, or runtime&#x27;. The README, docs quickstart list and sitemap have Node.js, Bun and TypeScript samples but no Deno-specific guide or sample.</p>

<p>https://raw.githubusercontent.com/keploy/keploy/main/README.md — Records API calls and database queries and replays them as tests. Records Postgres, MySQL, MongoDB, Kafka and RabbitMQ. eBPF capture &#x27;works with any language, framework, or runtime&#x27;. No mention of Deno.</p>

<p>https://keploy.io/docs/sitemap.xml — Quickstarts include samples-nodejs, samples-bunjs, samples-typescript and samples-redis, but no Deno page. keploy.io/docs/quickstart/deno/ and /samples-deno/ return 404.</p>

<p>https://github.com/keploy/keploy — Not archived. Current description: &#x27;Open-source platform for creating safe, isolated production sandboxes for API, integration, and E2E testing.&#x27;</p>

<p>Blocking questions: Unresolved: whether Keploy officially supports or documents Deno, or only claims generic runtime-agnostic support. This determines fit in Modules / Testing.</p>

<p>Caveats: Did not run Keploy against a Deno app.; &#x27;fetch calls&#x27; is JS-flavored wording for outbound HTTP; Keploy intercepts at the network layer, not the fetch API.</p>

</details>

<h3>rubico — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>Rubico is live and still describes &#x27;[A]synchronous Functional Programming&#x27;, so the function-composition description broadly holds. Its fit in a Deno catalog is unresolved. The current README has no Deno mention; it documents npm, CommonJS, browser CDN and Node ESM only. deno.land/x/rubico tops out at v1.3.1, while npm package.json is 2.24.0. Unknown: whether the maintainers still support or target Deno, for example via npm: specifiers.</p>

<p>https://raw.githubusercontent.com/a-synchronous/rubico/master/README.md — The heading is &#x27;[A]synchronous Functional Programming&#x27;. Installation covers npm, Node CommonJS, browser script tags and Node ESM. A case-insensitive search for &#x27;deno&#x27; found 0 matches.</p>

<p>https://raw.githubusercontent.com/a-synchronous/rubico/master/package.json — name rubico, version 2.24.0, description &#x27;[a]synchronous functional programming&#x27;.</p>

<p>https://cdn.deno.land/rubico/meta/versions.json — The latest deno.land/x version is v1.3.1, far behind npm 2.24.0. https://deno.land/x/rubico redirects to @v1.3.1.</p>

<p>Blocking questions: Unresolved whether Rubico is still intended or supported for Deno users; the README dropped Deno and the deno.land/x releases stopped at v1.3.1.</p>

<p>Caveats: Rubico may still work in Deno via npm:rubico; this was not tested.; No JSR package was found at @rubico/rubico; other scopes were not searched exhaustively.</p>

</details>

<h3>nest.land — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The nest.land homepage returns 200, but it is a JS-only SPA with no readable text. The official docs (docs.nest.land) still describe &quot;a first-of-its-kind immutable module registry and CDN built for Deno&quot; that publishes to the Arweave Permaweb. That supports the description. However, the module CDN x.nest.land timed out repeatedly from my environment, and most nestdotland service repos (api, cdn, db) were last pushed in 2023 and marked WIP. Unresolved: whether nest.land currently still serves modules and accepts publishes. The timeout may be transient or a network issue on my side.</p>

<p>https://docs.nest.land — &quot;nest.land is a first-of-its-kind immutable module registry and CDN built for Deno... publish your Deno modules to the Arweave Permaweb, where they can never be deleted or modified.&quot;</p>

<p>https://nest.land — HTTP 200. A JS-only SPA whose static HTML contains only the title &quot;nest.land&quot; and loader scripts.</p>

<p>https://x.nest.land/ — The connection timed out (curl exit 28) on repeated attempts. It may be a transient or environment-specific failure, so recheck.</p>

<p>https://api.github.com/orgs/nestdotland/repos — Most recent activity is the template repo (2026-11-01). The nest.land website repo was last pushed 2024-01. The api, cdn and db repos were last pushed 2023-03 and are labeled [WIP].</p>

<p>Blocking questions: It is unknown whether the x.nest.land module CDN is operational. It timed out from my environment.</p>

<p>Caveats: The homepage requires JavaScript, so I could not read its current content.; Access failures do not prove the service is dead.</p>

</details>

<h3>The Official Showcase — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>https://deno.land/showcase 301-redirects to https://deno.com/showcase. That URL returns HTTP 200 but renders a page titled &#x27;Not Found | Deno&#x27; (a soft 404). It has no showcase content and is not linked from the deno.com homepage nav. No Wayback snapshot was returned for deno.com/showcase, and I found no official replacement page. The current deno.com/customers path is also a soft 404. Unresolved: whether the official showcase was intentionally retired, moved to another URL, or is temporarily broken.</p>

<p>https://deno.land/showcase — HTTP 301, location: https://deno.com/showcase.</p>

<p>https://deno.com/showcase — HTTP 200 with &lt;title&gt;Not Found | Deno&lt;/title&gt;; no showcase listing content present.</p>

<p>https://deno.com/ — Homepage nav links include /blog, /deploy, /enterprise, /pricing, /manual; no showcase link found.</p>

<p>https://archive.org/wayback/available?url=deno.com/showcase — Returned no archived snapshots.</p>

<p>Blocking questions: No official statement found that the showcase was retired, and no official relocated URL was found. Removal or update cannot yet be justified.</p>

<p>Caveats: Soft-404 could be temporary; recheck recommended before acting.; Did not search Deno&#x27;s website source repository for a relocated showcase.</p>

</details>

<h3>denopendabot — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The GitHub App page still loads and describes keeping Deno project dependencies up to date. However, the source repo hasundue/denopendabot is described as &#x27;Dependabot for Deno projects (deprecated)&#x27;, and its README says it &#x27;is deprecated in favor of renovate or molt&#x27;. Molt in turn recommends Deno&#x27;s built-in `deno outdated --update` (Deno ≥2.1). The deprecation is official, but no single successor is documented (Renovate is a third-party competitor; molt is one of two options). It is also unconfirmed whether the hosted App still runs. The maintainer must choose between removing the entry and replacing it with molt.</p>

<p>https://github.com/apps/denopendabot — HTTP 200; &#x27;Denopendabot keeps the dependencies of your Deno projects up-to-date... Written in Deno, and running on Deno Deploy.&#x27;</p>

<p>https://api.github.com/repos/hasundue/denopendabot — archived=false, pushed_at 2024-06-17, description &#x27;Dependabot for Deno projects (deprecated)&#x27;.</p>

<p>https://github.com/hasundue/denopendabot — README warning: &#x27;Denopendabot is deprecated in favor of renovate or molt.&#x27;</p>

<p>https://github.com/hasundue/molt — Molt README: &#x27;Now Deno has a built-in command to update dependencies (deno outdated --update) as of v2.1. It is recommended to use that instead, if you manage your dependencies in deno.json(c).&#x27;</p>

<p>Blocking questions: Two alternatives are named in the deprecation notice (Renovate, a competitor, and molt), so no single documented successor exists for a replace.; Unknown whether the hosted GitHub App still functions; removal relies on deprecation rather than confirmed loss of function.</p>

<p>Caveats: Did not install or exercise the GitHub App.; The packet&#x27;s source snapshot for this URL failed; the evidence above was gathered directly.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Berkenalan dengan Deno — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>No version of the article could be read. Medium returned a Cloudflare challenge (403) on both the medium.com URL and the medium.easyread.co redirect target, and the Wayback Machine has no capture. Whether the article still exists and what it contains are unverified. This is an access failure, not evidence the article is gone.</p>

<p>Blocking questions: The article&#x27;s existence and content could not be read from any source.</p>

<p>Caveats: The packet&#x27;s snapshot recorded a redirect to medium.easyread.co, which suggests the post was moved into a publication rather than deleted, but I could not confirm this.; Recheck from a normal browser.</p>

</details>

<h3>Telegram chat — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>@denoland is a live Telegram group titled &#x27;Deno [chat]&#x27;, but nothing on its public page shows it is Russian-language. That leaves its fit in the Russian section unresolved.</p>

<p>https://t.me/denoland — HTTP 200. og:title &#x27;Deno [chat]&#x27;, 84 members. Description is only &#x27;Denoland https://github.com/denoland&#x27;. Messages are not publicly previewable (t.me/s/denoland returned no content).</p>

<p>Blocking questions: The language and affiliation of the chat could not be verified, so its fit in the Russian section is unconfirmed.</p>

<p>Caveats: The group may be the discussion chat linked to the Russian @denoland_ru channel (same &#x27;Denoland&#x27; naming), but I could not confirm that.</p>

</details>

<h3>Design Mistakes in Node zh-CN — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>An archived copy confirms this is a full Chinese translation of Ryan Dahl&#x27;s 2018 &#x27;Design Mistakes in Node&#x27; talk, which mentions Deno. Current availability is unverified: the live fetch hit Zhihu&#x27;s anti-bot wall (403), and the newest archive (2024) also captured only that wall.</p>

<p>http://web.archive.org/web/20200929214937/https://zhuanlan.zhihu.com/p/37637923 — Title &#x27;《Design Mistakes in Node》Node 之父 Ryan Dahl 演讲 PPT 中文版 (2018 JS Conf Berlin) - 知乎&#x27;. The description says it is the complete Chinese translation of the talk and recommends it to readers interested in Node and Deno.</p>

<p>https://zhuanlan.zhihu.com/p/37637923 — Live fetch returned HTTP 403 (anti-bot). The September 2024 Wayback capture shows only Zhihu&#x27;s zse-ck anti-bot shell, not the article.</p>

<p>Blocking questions: Current availability could not be confirmed; the last readable copy is from September 2020.</p>

<p>Caveats: Zhihu routinely blocks automated clients. Recheck in a browser. This access failure is not evidence the article was removed.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<details>
<summary>43 unresolved keeps</summary>

These entries were not added to the baseline.

<h3>Deno Standard Library — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>https://jsr.io/@std returns HTTP 200. The scope page says &#x27;This is the Deno standard library&#x27; and lists the current @std packages, for example @std/assert v1.0.19 and @std/async v1.5.1. The link is the correct official location.</p>

<p>https://jsr.io/@std — HTTP 200. The page says &#x27;This is the Deno standard library. Read more about it https://docs.deno.com/runtime/fundamentals/standard_library/&#x27; and lists the @std packages and their versions.</p>

</details>

<h3>Official Site — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>https://deno.com returns HTTP 200 and is the official Deno homepage (current release banner v2.9, built-in toolchain). It fits Official Docs.</p>

<p>https://deno.com — HTTP 200. The title is &#x27;Deno, the drop-in JavaScript runtime for Node developers&#x27;. The page shows a v2.9 &#x27;What&#x27;s new&#x27; link, a list of built-in tools and a &#x27;Deno is joining Cloudflare!&#x27; banner.</p>

<p>Caveats: The homepage banner announces &#x27;Deno is joining Cloudflare&#x27;. This does not affect this link today, but the domain or branding could change later.</p>

</details>

<h3>@iuioiua/redis — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The JSR page for @iuioiua/redis (1.1.10) uses this exact tagline: &#x27;Fast, lightweight Redis client built upon the Web Streams API.&#x27; It shows a Deno usage example.</p>

<p>https://jsr.io/@iuioiua/redis — HTTP 200, v1.1.10. It works with Browsers, Deno, Node.js, Cloudflare Workers and Bun, and has a JSR score of 100%. Tagline: &#x27;Fast, lightweight Redis client built upon the Web Streams API.&#x27; The example uses Deno.connect.</p>

<p>Caveats: Latest publish was 11 months ago. JSR notes a known issue with replies containing CRLF.</p>

</details>

<h3>dinoenv — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>deno.land/x/dinoenv resolves to v1.1.0, uploaded 2021-03-04 from crewdevio/dino_env. That GitHub repo still exists and is not shown as archived. The published README (&#x27;manage environment variables with deno&#x27;) and mod.ts (a config() function that loads a .env file into Deno.env) match the entry. The package snapshot was unavailable only because no GitHub source was recorded for the entry.</p>

<p>https://cdn.deno.land/dinoenv/meta/versions.json — latest v1.1.0. Versions are v1.1.0 and v1.0.0.</p>

<p>https://cdn.deno.land/dinoenv/versions/v1.1.0/meta/meta.json — uploaded_at 2021-03-04. upload_options are github, repository crewdevio/dino_env, ref v1.1.0.</p>

<p>https://cdn.deno.land/dinoenv/versions/v1.1.0/raw/mod.ts — Exports config({path, encoding}). It reads a .env file with Deno.readFileSync and sets each parsed key with Deno.env.set.</p>

<p>https://github.com/crewdevio/dino_env — HTTP 200. Page title &#x27;GitHub - crewdevio/dino_env: manage environment variables with deno.&#x27; No archive banner was detected.</p>

<p>Caveats: The last release was in 2021. Behavior under Deno 2.x was not tested.; Style only: the description starts in lowercase, has no capitalized &#x27;Deno&#x27;, and uses &#x27;(for) Deno&#x27;-style phrasing. Optional wording: &#x27;Tiny library to manage environment variables.&#x27;; The GitHub API was rate-limited, so archived status was inferred from the HTML page only.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>locale-kit — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The main library resolves at deno.land/x/localekit (latest 2.2.0, uploaded 2024-03-17 from locale-kit/locale-kit) and at JSR @locale-kit/locale-kit 2.2.0. Its docs cover dynamic string replacement and match cases &#x27;used primarily for things like plurals&#x27;. The Fresh wrapper claim is supported by the organization&#x27;s separate locale-kit-fresh repo, published as deno.land/x/localekit_fresh (latest 0.5.2), whose README describes &#x27;A small wrapper for Fresh to handle translations via locale-kit&#x27;. Both linked URLs are reachable.</p>

<p>https://cdn.deno.land/localekit/versions/2.2.0/meta/meta.json — uploaded_at 2024-03-17. upload_options are github, repository locale-kit/locale-kit, ref 2.2.0.</p>

<p>https://raw.githubusercontent.com/locale-kit/locale-kit/HEAD/deno.json — name @locale-kit/locale-kit, version 2.2.0, exports ./mod.ts. The mod.ts LocaleKit class handles &#x27;translation/replacement of dynamic substrings&#x27;.</p>

<p>https://locale-kit.github.io/docs/usage/dynamic/match-cases/ — &#x27;LocaleKit comes with a set of predefined match cases for dynamic strings. These are used primarily for things like plurals, optional strings, etc.&#x27;</p>

<p>https://locale-kit.github.io/docs/guides/getting-started/installation/ — Deno install is &#x27;deno add @locale-kit/locale-kit&#x27;. Other runtimes use &#x27;jsr add&#x27;.</p>

<p>https://raw.githubusercontent.com/locale-kit/locale-kit-fresh/HEAD/README.md — &#x27;locale-kit (fresh wrapper)&#x27;. Imports languagePlugin from https://deno.land/x/localekit_fresh/mod.ts for Fresh start(). deno.land/x/localekit_fresh lists versions up to 0.5.2.</p>

<p>Caveats: The Fresh wrapper lives in a separate repo and module, not in locale-kit itself. The entry does not link it. A maintainer might add the link, but the claim is true at the project level.; The Fresh wrapper&#x27;s compatibility with current Fresh versions was not verified, and its last-update date was not retrieved.; Style only: &#x27;A internationalisation&#x27; should be &#x27;An internationalisation&#x27;. This is a multi-link entry, so any wording change must be made manually.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Deno Blog — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>deno.com/blog is live and remains Deno&#x27;s official blog, with recent posts on Deno 2.8, 2.9 and Deno Deploy. The description is accurate.</p>

<p>https://deno.com/blog — HTTP 200 with no redirect. Recent posts include &#x27;Deno is joining Cloudflare&#x27; (October 9, 2026), &#x27;Deno 2.9&#x27; (June 25, 2026) and &#x27;Deno 2.8&#x27; (May 22, 2026).</p>

<p>Caveats: The October 2026 post announces Deno joining Cloudflare, and the article was not read. &#x27;Deno Company&#x27; wording or the blog&#x27;s location could change later; recheck if the domain or ownership changes.</p>

</details>

<h3>Deno News — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>deno.news is Deno Land Inc.&#x27;s official newsletter. The page still uses the catalog&#x27;s exact tagline, and the official Buttondown RSS feed shows recent issues, the latest dated Aug 2025.</p>

<p>https://deno.news/ — HTTP 200 on a deno.com-branded page (Copyright 2026 Deno Land Inc.). The heading reads &#x27;Deno News - A newsletter of Deno articles, news and cool projects.&#x27; A static fetch showed &#x27;0 subscribers - 0 issues&#x27;, which looks like a client-rendered placeholder.</p>

<p>https://buttondown.com/denonews/rss — The RSS feed linked from deno.news has 30 items. The latest are &#x27;Deno 2.4, Databases on Deno Deploy, and more&#x27; (14 Aug 2025), &#x27;Josh shows us his doodles&#x27; (25 Jun 2025) and &#x27;A sneak peek at the new Deno Deploy&#x27; (5 Jun 2025).</p>

<p>Caveats: No issue found after Aug 2025, so how often it publishes now is unknown. The description makes no claim about frequency.</p>

</details>

<h3>Develop with Deno and Visual Studio Code — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Kitson Kelly&#x27;s dated (Jan 2019) Medium article on developing Deno with VS Code. Medium blocked the direct fetch with a Cloudflare challenge, but a Wayback snapshot confirms the title, author and URL. It is a historical article and fits the Articles section.</p>

<p>https://medium.com/@kitsonk/develop-with-deno-and-visual-studio-code-225ce7c5b1ba — Direct fetch returned HTTP 403 with a Cloudflare &#x27;Just a moment...&#x27; challenge. This is a bot block, not proof the article is gone.</p>

<p>http://web.archive.org/web/20250219055942/https://medium.com/@kitsonk/develop-with-deno-and-visual-studio-code-225ce7c5b1ba — Feb 2025 snapshot: title &#x27;Develop with Deno and Visual Studio Code | by Kitson Kelly | Medium&#x27;, datePublished 2019-01-15.</p>

<p>Caveats: The live page could not be read directly because of the bot challenge. Availability rests on a Feb 2025 archive snapshot.; The tooling described is from 2019 and may predate the official Deno VS Code extension. It is kept as a dated resource.</p>

</details>

<h3>Deno on Cloud Run — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Grant Timmerman&#x27;s &#x27;Deno on Cloud Run&#x27; article in the Google Cloud Community Medium publication, published May 2020. The direct fetch hit a Cloudflare challenge, but an Oct 2026 Wayback capture of the URL returned 200 with matching metadata.</p>

<p>https://medium.com/google-cloud/deno-on-cloud-run-89ae64d1664d — Direct fetch returned HTTP 403 with a Cloudflare challenge (a bot block).</p>

<p>http://web.archive.org/web/20220110212528/https://medium.com/google-cloud/deno-on-cloud-run-89ae64d1664d — Title &#x27;Deno on Cloud Run. 🦕 Deno is a secure TypeScript runtime… | by Grant Timmerman | Google Cloud - Community | Medium&#x27;.</p>

<p>http://web.archive.org/web/20261022142543/https://medium.com/google-cloud/deno-on-cloud-run-89ae64d1664d — Oct 2026 capture returned 200 with datePublished 2020-05-13, so the article was still served recently.</p>

<p>Caveats: The live page could not be read directly. The Cloud Run and Deno steps date from 2020.</p>

</details>

<h3>Create your first News CLI app using Deno — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Bhumij Gupta&#x27;s article in JavaScript In Plain English, published June 2020. The medium.com URL redirects to the publication&#x27;s custom domain, javascript.plainenglish.io. Direct fetches hit a Cloudflare 403, but a Wayback snapshot confirms the title and author.</p>

<p>https://medium.com/javascript-in-plain-english/creating-your-first-news-cli-app-using-deno-e1470398c627 — Direct fetch returned HTTP 403 with a Cloudflare challenge. The packet snapshot shows a redirect to javascript.plainenglish.io/creating-your-first-news-cli-app-using-deno-e1470398c627.</p>

<p>http://web.archive.org/web/20201031205742/https://medium.com/javascript-in-plain-english/creating-your-first-news-cli-app-using-deno-e1470398c627 — Title &#x27;Creating your first News CLI app using Deno | by Bhumij Gupta | JavaScript In Plain English | Medium&#x27;, datePublished 2020-06-01.</p>

<p>Caveats: The catalog says &#x27;Create&#x27; while the article title says &#x27;Creating&#x27;. This is a minor wording difference.; The canonical URL could be the javascript.plainenglish.io domain. I could not confirm it live because of the 403, so I am not proposing a URL change.</p>

</details>

<h3>Getting Started with Deno — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The live Sabe tutorial&#x27;s headline matches: an introduction to the Deno runtime.</p>

<p>https://sabe.io/tutorials/getting-started-with-deno — HTTP 200. Headline &#x27;Getting Started with Deno | Sabe&#x27;; description &#x27;Get started with the new JavaScript runtime Deno...&#x27;.</p>

<p>Caveats: No publication date found in the static HTML.</p>

</details>

<h3>How to deploy a Deno app using Docker — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The live Sabe tutorial&#x27;s headline matches: deploying a Deno app with Docker and Docker Compose.</p>

<p>https://sabe.io/tutorials/how-to-deploy-deno-app-docker — HTTP 200. Headline &#x27;How to deploy a Deno app using Docker | Sabe&#x27;; description mentions Docker Compose and Dockerfile.</p>

<p>Caveats: No publication date found. The Docker image references were not checked.</p>

</details>

<h3>10 Things I Regret About Node.js - Ryan Dahl - JSConf EU 2018 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Ryan Dahl&#x27;s 2018 JSConf EU talk introducing Deno, a landmark historical presentation. The video is playable on the official JSConf channel.</p>

<p>https://www.youtube.com/watch?v=M3BM9TB-8yA — HTTP 200. Title &#x27;10 Things I Regret About Node.js - Ryan Dahl - JSConf EU&#x27;; channel JSConf; uploaded 2018-06-06; playabilityStatus OK.</p>

<p>Caveats: The YouTube title omits &#x27;2018&#x27;. The catalog&#x27;s added year is accurate context.</p>

</details>

<h3>JSDC 2018#A01 - Deno, A New Server-Side Runtime By Ryan Dahl — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Ryan Dahl&#x27;s JSDC 2018 talk on Deno is playable on the official JSDC.tw channel, and the title matches exactly. It is a historical presentation.</p>

<p>https://www.youtube.com/watch?v=FlTG0UXRAkE — HTTP 200. Title &#x27;JSDC 2018#A01 - Deno, A New Server-Side Runtime By Ryan Dahl&#x27;; channel JSDC.tw; uploaded 2018-11-27; playabilityStatus OK.</p>

<p>Caveats: Did not watch the video.</p>

</details>

<h3>Ryan Dahl. Deno, a new way to JavaScript. JS Fest 2019 Spring — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The video is live on the JS Fest organizer&#x27;s (Fest Group) YouTube channel. Its title matches the catalog entry: speaker, talk title and event. It is a dated historical Deno talk and fits the Presentations section.</p>

<p>https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=z6JRlx5NC9E&amp;format=json — oEmbed title: &#x27;Deno, a new way to JavaScript. Ryan Dahl. JS Fest 2019 Spring&#x27;. Author: Fest Group.</p>

<p>Caveats: I did not watch the video. I checked only the metadata.</p>

</details>

<h3>Rafał Pocztarski — From Node.js to Deno - JavaScript/TypeScript runtime built with V8 and Rust [EN] — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The video is live on the WarsawJS channel. Its title exactly matches the catalog entry&#x27;s name. It is a historical Deno talk and fits Presentations.</p>

<p>https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=Aib1OZLy0_c&amp;format=json — oEmbed title: &#x27;Rafał Pocztarski — From Node.js to Deno - JavaScript/TypeScript runtime built with V8 and Rust [EN]&#x27;. Author: WarsawJS.</p>

<p>Caveats: I did not watch the video.</p>

</details>

<h3>Ryan Dahl: A secure runtime for JavaScript and TypeScript | js.la April 2019 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The video is live on the js.la channel. Its title exactly matches the catalog entry&#x27;s name. It is a historical Deno talk.</p>

<p>https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=RAmqgbv247s&amp;format=json — oEmbed title: &#x27;Ryan Dahl: A secure runtime for JavaScript and TypeScript | js.la April 2019&#x27;. Author: js.la.</p>

<p>Caveats: I did not watch the video.</p>

</details>

<h3>Slides — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Google Slides deck is publicly reachable. Its title, &#x27;deno JS.LA&#x27;, matches the parent js.la talk.</p>

<p>https://docs.google.com/presentation/d/1CSQVTeH5tFzE4AZVXIpx9Xwew5YS-gxJZ03eRFtNeIc/edit — HTTP 200. og:title: &#x27;deno JS.LA&#x27;.</p>

<p>Caveats: I did not check who owns the deck. It is linked as slides for the parent talk.</p>

</details>

<h3>Ryan Dahl: Deno, a new way to JavaScript - HolyJS 2019 Piter — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The video is live on the official HolyJS channel. Its title is &#x27;Ryan Dahl — Deno, a new way to JavaScript&#x27; and it was published on 2019-08-28. Its description is the Deno talk abstract. The catalog&#x27;s wording (&#x27;HolyJS 2019 Piter&#x27;) adds event context but is accurate.</p>

<p>https://www.youtube.com/watch?v=HjdJzNoT_qg — oEmbed author: HolyJS. Title: &#x27;Ryan Dahl — Deno, a new way to JavaScript&#x27;. publishDate: 2019-08-28. The description is a Deno abstract.</p>

<p>Caveats: The YouTube metadata does not itself name &#x27;Piter 2019&#x27;. I inferred the event from the HolyJS channel and the 2019 date.</p>

</details>

<h3>Slides — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Google Slides deck titled &#x27;holyjs&#x27; is publicly reachable. This matches the parent HolyJS talk.</p>

<p>https://docs.google.com/presentation/d/1BjvZx5S8noVfFINptH4jfKfqh9jB9nXlFC0I3oIDtg4/edit — HTTP 200. og:title: &#x27;holyjs&#x27;.</p>

<p>Caveats: I did not review the slide contents in detail.</p>

</details>

<h3>Rafał Pocztarski - What is Deno? A new runtime for modern JavaScript and TypeScript backends for 2020s - Deno Warsaw — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The video is live on the Deno Warsaw channel. Its description gives the full title used in the catalog. The video was recorded at the Deno Warsaw #1 meetup in 2019.</p>

<p>https://www.youtube.com/watch?v=aI5A9zvYSjk — Title: &#x27;What is Deno? by Rafał Pocztarski - Deno Warsaw #1 [EN]&#x27;. The description begins: &#x27;What is Deno? A new runtime for modern JavaScript and TypeScript backends for 2020s by Rafał Pocztarski&#x27;. Published 2019-10-25.</p>

<p>Caveats: I did not watch the video.</p>

</details>

<h3>Michał Sabiniarz - How to contribute to Deno? - Deno Warsaw — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The video is live on the Deno Warsaw channel, and the speaker and topic match. It is a historical talk on contributing to Deno.</p>

<p>https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=LAtjnKLbPpw&amp;format=json — oEmbed title: &#x27;How to contribute to Deno? by Michał Sabiniarz - Deno Warsaw #1 [EN]&#x27;. Author: Deno Warsaw.</p>

<p>Caveats: The contribution process described in this 2019 talk may differ from today&#x27;s process. That makes it a dated resource, not a reason to remove it.</p>

</details>

<h3>Bartek Iwańczuk - Deno internals, how modern runtime is built - Deno Warsaw — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The video is live on the Deno Warsaw channel. Its title is &#x27;Deno internals by Bartek Iwańczuk&#x27;. The linked slides use the full title &#x27;Deno internals - how modern runtime is built&#x27;, which supports the catalog name.</p>

<p>https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=qt7fbmypAFk&amp;format=json — oEmbed title: &#x27;Deno internals by Bartek Iwańczuk - Deno Warsaw #1 [EN]&#x27;. Author: Deno Warsaw.</p>

<p>Caveats: The internals described in 2019 have changed since then. This is a dated historical resource.</p>

</details>

<h3>Slides — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Google Slides deck is publicly reachable, and its title matches the parent talk.</p>

<p>https://docs.google.com/presentation/d/1LYNGpyjx9PemL-P__7hVC8mSqkX-jL8VQLMhCRehy00/edit?usp=sharing — HTTP 200. og:title: &#x27;Deno internals - how modern runtime is built&#x27;.</p>

<p>Caveats: I did not review the slide contents in detail.</p>

</details>

<h3>Ryan Dahl &amp; Kitson Kelly: Deno is a New Way to JavaScript - TSConf 2019 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The video is live on the SitePen channel. Its title matches the speakers and topic, and its description begins &#x27;TSConf 2019&#x27;.</p>

<p>https://www.youtube.com/watch?v=1gIiZfSbEAE — oEmbed title: &#x27;Deno is a New Way to JavaScript - Ryan Dahl &amp; Kitson Kelly&#x27;. Author: SitePen. The description begins &#x27;TSConf 2019&#x27;. Published 2019-12-19.</p>

<p>Caveats: I did not watch the video.</p>

</details>

<h3>Bert Belder - Deno - dotJS 2019 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The video is live on the official dotconferences channel. The speaker, event and topic match.</p>

<p>https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=puXyo1jGQys&amp;format=json — oEmbed title: &#x27;dotJS 2019 - Bert Belder - Deno&#x27;. Author: dotconferences.</p>

<p>Caveats: I did not watch the video.</p>

</details>

<h3>Kitson P. Kelly - Deno, and The Future of JavaScript Runtimes - CityJS Conf 2020 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The video is live on the Pusher channel, which organises CityJS. Its title exactly matches the catalog entry&#x27;s name.</p>

<p>https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=2eRyZpX4qvI&amp;format=json — oEmbed title: &#x27;Deno, and The Future of JavaScript Runtimes - Kitson P. Kelly - CityJS Conf 2020&#x27;. Author: Pusher.</p>

<p>Caveats: I did not watch the video.</p>

</details>

<h3>Matías Insaurralde - Deno: an experimental approach on V8 interoperability [EN subtitles] - NodeConf Argentina 2019 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The video is live on the NodeConf Argentina channel, and the speaker and title match. It was published on 2019-11-09.</p>

<p>https://www.youtube.com/watch?v=N0BRE-0n2cU — oEmbed title: &#x27;Matias Insaurralde - Deno: an experimental approach on V8 interoperability&#x27;. Author: NodeConf Argentina. Published 2019-11-09.</p>

<p>Caveats: I did not verify the &#x27;[EN subtitles]&#x27; claim in the name. I did not inspect the caption tracks.</p>

</details>

<h3>Slides — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Speaker Deck page is live under the speaker&#x27;s account, and its title matches the parent talk.</p>

<p>https://speakerdeck.com/matiasinsaurralde/deno-an-experimental-approach-on-v8-interoperability — HTTP 200. og:title: &#x27;Deno: an experimental approach on V8 interoperability&#x27;. The account is matiasinsaurralde.</p>

</details>

<h3>Modern Web Development with Deno — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL returned HTTP 429 (rate limited) to every request, so the packet&#x27;s fetch failure looks temporary, not a dead link. According to search results, the book is Mayur Borse&#x27;s &#x27;Modern Web Development with Deno&#x27; (BPB Publications, 2022, ISBN 9789355510969). Those results also cite a matching BPB product page at in.bpbonline.com, which also returned 429 when fetched. It is a Deno book and fits Books.</p>

<p>https://bpbonline.com/products/modern-web-development-with-deno — Returned HTTP 429 with Retry-After: 60 to curl and WebFetch on repeated tries. Rate limited, not missing.</p>

<p>https://in.bpbonline.com/products/modern-web-development-with-deno — According to search results, BPB lists the book here with the same product slug. A direct fetch returned HTTP 429, so I could not read the page.</p>

<p>https://www.overdrive.com/media/9392091/modern-web-development-with-deno — According to search results, OverDrive lists &#x27;Modern Web Development with Deno&#x27; by Mayur Borse. I did not open this page myself.</p>

<p>Caveats: I could not read the listed BPB product page or its regional equivalent because of rate limiting (429). Recheck that the bpbonline.com page still exists before closing this item.; The book dates from 2022, before Deno 2. That makes it a dated resource, not grounds for removal.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>让我们一起来学习别人学不动的 Deno — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>When fetched again, the SegmentFault article returned HTTP 200. Its title is &#x27;node.js - 让我们一起来学习别人学不动的deno&#x27;. The packet&#x27;s timeout was transient. It is a 2018 Chinese introduction to early Deno and fits the Chinese resources section.</p>

<p>https://segmentfault.com/a/1190000015151287 — HTTP 200. Page title: &#x27;node.js - 让我们一起来学习别人学不动的deno - 日新亭 - SegmentFault 思否&#x27;. WebFetch summary: author 张京, published 2018-06-03, an introduction to Deno with install and build instructions.</p>

<p>Caveats: The install and build steps are from 2018 and outdated. That is expected for a dated article.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Node之父ry：Node中的设计错误 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The WeChat article still serves its content: a Chinese translation of Ryan Dahl&#x27;s 2018 JSConf EU talk on design mistakes in Node, which covers Deno. It is a dated historical resource and fits the Chinese section.</p>

<p>https://mp.weixin.qq.com/s/7XAiYw18c8YZc-fXk0-wrw — HTTP 200. og:title is &#x27;Node之父ry：Node中的设计错误&#x27;, published by account 前端之巅, ct timestamp 1528088680 (June 2018). js_content says the piece is a translation of Ryan Dahl&#x27;s June 2018 Berlin JS conference talk and covers Deno&#x27;s design (URL imports, built-in TypeScript compiler).</p>

<p>Caveats: The packet snapshot hit a WeChat captcha page, but a direct fetch returned the full article. Future automated checks may hit the captcha again.</p>

</details>

<h3>Node之父 - Deno，一个新的JS运行时 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Bilibili video is live. Its title matches the entry (a Chinese-English subtitled upload of Ryan Dahl&#x27;s Deno talk), so it fits the Chinese section.</p>

<p>https://www.bilibili.com/video/av52038617/ — HTTP 200, title &#x27;【中英双语】Node之父 - Deno，一个新的JS运行时_哔哩哔哩_bilibili&#x27;, bvid BV124411Y74C.</p>

<p>http://web.archive.org/web/20250127193017/https://www.bilibili.com/video/av52038617/ — January 2025 archive shows the same title and pubdate 1557490281 (May 2019).</p>

<p>Caveats: Did not watch the video. The av-number URL still resolves, but the BV id is Bilibili&#x27;s current canonical form.</p>

</details>

<h3>Deno intro in Hebrew (slides in English) — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The YouTube video is playable. It is Benjamin Gruenbaum&#x27;s Deno talk in Hebrew at a JavaScript Israel meetup in June 2018, which fits the Hebrew section.</p>

<p>https://www.youtube.com/watch?v=9tJ_LkI6_qw — playabilityStatus OK. Title &#x27;Deno - Benjamin Gruenbaum (Hebrew)&#x27;, channel &#x27;JavaScript Israel&#x27;, published 2018-07-18. The description says it is a lecture about Deno given at a JavaScript Israel Meetup on 27/06/18.</p>

<p>Caveats: Did not watch the video, so the &#x27;(slides in English)&#x27; detail is unverified.</p>

</details>

<h3>Perkenalan Deno dan Instalasi — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The video is playable. It is an Indonesian Deno introduction covering installation, Hello World, a server and a REST API, which matches the entry name and the Indonesian section.</p>

<p>https://www.youtube.com/watch?v=V_kpUTJSd9c — playabilityStatus OK. Channel &#x27;devindo&#x27;, published 2020-05-17. The YouTube title is &#x27;Deno - A secure runtime for JavaScript and TypeScript&#x27;. The description reads &#x27;Pengenalan deno, dan membuat api sederhana dengan deno&#x27; with chapters Introduction Deno, Instalasi, Hello World, Membuat Server, Membuat REST API.</p>

<p>Caveats: The catalog name &#x27;Perkenalan Deno dan Instalasi&#x27; is a descriptive Indonesian label, not the video&#x27;s literal YouTube title. It is still accurate.</p>

</details>

<h3>Deno Land Indonesia Telegram group — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Telegram group @deno_id is live, titled Deno.ID, and links to denoland.id, so it is an Indonesian Deno community. The entry name and section fit.</p>

<p>https://t.me/deno_id — HTTP 200. og:title &#x27;Deno.ID&#x27;, 437 members. Description: &#x27;A secure runtime for JavaScript and TypeScript built with V8, Rust, and Tokio - https://denoland.id&#x27;.</p>

<p>Caveats: Group messages are not publicly previewable, so current activity and language of discussion were not verified.</p>

</details>

<h3>mizchi/deno_code_reading.md — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>mizchi&#x27;s gist deno_code_reading.md is live under the listed owner, and its title matches the entry. It is a dated (2019) Japanese reading of Deno&#x27;s source code and remains valid as a historical resource.</p>

<p>https://gist.github.com/mizchi/31e5628751330b624a0e8ada9e739b1e — HTTP 200, title &#x27;deno_code_reading.md&#x27;, owner mizchi. Page contains many Deno references. Comment/revision datetimes are around 2019-01-08/09.</p>

<p>Caveats: The gist describes a 2019 Deno codebase and does not reflect current internals.</p>

</details>

<h3>Design Mistakes in Node &amp; Deno #kng5 / deno — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Speaker Deck deck is live with exactly the listed title, published 2019-02-01. It fits the Japanese section.</p>

<p>https://speakerdeck.com/masashi/deno — HTTP 200, title &#x27;Design Mistakes in Node &amp; Deno #kng5 / deno - Speaker Deck&#x27;, datePublished 2019-02-01.</p>

<p>Caveats: Did not review the deck&#x27;s slide content in detail.</p>

</details>

<h3>Telegram channel — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>@denoland_ru is a live, Russian-language Deno news channel and still posts. Its most recent visible post is from 2026-10-10. It fits the Russian section.</p>

<p>https://t.me/denoland_ru — HTTP 200, og:title &#x27;Denoland&#x27;, 90 subscribers. Description: &#x27;Всё про Deno: релизы, новости, статьи и т.д.&#x27; (Russian: &#x27;Everything about Deno: releases, news, articles, etc.&#x27;).</p>

<p>https://t.me/s/denoland_ru — The public preview shows Russian posts about Deno releases (including Deno 2.0). The latest post is dated 2026-10-10T13:35:02Z.</p>

<p>Caveats: Channel post content is untrusted and was not used to judge anything beyond activity and language.</p>

</details>

<h3>Hola Deno! . 🦕 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Spanish &#x27;Hola Deno!&#x27; article exists at the listed URL in a January 2025 Wayback capture, with a matching title and a 2020 publication date. The live fetch was blocked by a Cloudflare challenge, which is not evidence of removal.</p>

<p>http://web.archive.org/web/20250127192819/https://medium.com/javascript-espa%C3%B1ol/hola-deno-f31f9f6f2c84 — Title &#x27;Hola Deno! . 🦕 ... | by Francisco Suarez | Guanaco JS | Medium&#x27;, datePublished 2020-05-14. Description: &#x27;El día de hoy hablaremos de Deno y crearemos nuestro primer Hola Mundo.&#x27;</p>

<p>Caveats: Live medium.com returned a 403 Cloudflare challenge. The most recent readable copy is from January 2025.; The publication now appears under the name Guanaco JS. The URL slug still resolves.</p>

</details>

<h3>Así puedes crear tu primera API REST con Deno — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>A September 2024 Wayback capture shows the Spanish REST API tutorial by Marc Pàmpols with the matching title, at the subdomain URL the packet snapshot redirected to. The live fetch was blocked by Cloudflare.</p>

<p>http://web.archive.org/web/20240928225525/https://mpampols.medium.com/as%C3%AD-puedes-crear-tu-primera-api-rest-con-deno-a9094ee5c0b2 — Title &#x27;Así puedes crear tu primera API REST con Deno | by Marc Pàmpols | Medium&#x27;, datePublished 2020-05-23.</p>

<p>Caveats: Live Medium returned a 403 Cloudflare challenge. The listed medium.com/@ URL redirects to Medium&#x27;s standard user subdomain, so no URL change is needed.</p>

</details>

<h3>Primeros pasos con Deno 🦕 El sucesor de NodeJS desarrollado con Rust y TypeScript — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>A January 2025 Wayback capture shows Manu Rúa&#x27;s Spanish getting-started article at the listed URL with a matching title. The live fetch was blocked by Cloudflare.</p>

<p>http://web.archive.org/web/20250127192819/https://medium.com/@manurua/primeros-pasos-con-deno-el-nuevo-nodejs-desarrollado-con-rust-y-typescript-b9ac14f7d0c7 — Title &#x27;Primeros pasos con Deno 🦕 El sucesor de NodeJS desarrollado con Rust y TypeScript | by Manu Rúa | Medium&#x27;, datePublished 2020-05-17. Description: &#x27;¿Qué es Deno? Instalación y en qué se diferencia de NodeJS&#x27;.</p>

<p>Caveats: Live Medium returned a 403 Cloudflare challenge. The most recent readable copy is from January 2025.</p>

</details>

<h3>A first look at Deno | BlaBlaConf 2021 🇲🇦 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The BlaBlaConf 2021 talk is playable on the GeeksBlaBla channel and its title matches the entry. It fits the Darija section.</p>

<p>https://www.youtube.com/watch?v=Y_etUvzAa4s — playabilityStatus OK. Title &#x27;A first look at Deno with Yasser Ameur El Idrissi | BlaBlaConf 2021 🇲🇦&#x27;, channel GeeksBlaBla, published 2021-12-18.</p>

<p>Caveats: Did not watch the video, so the language (Darija) was not verified directly.</p>

</details>

</details>

The complete research records remain local. This inventory contains all recommendations and unresolved entries from the saved initial review.

[One-entry integration example](https://github.com/bromanko/awesome-deno/blob/codex/catalog-inventory-preview/.um/catalog-inventory/checked-example.md). Saved research with real discussion-history and patch checks.
