# EXP-001 Protocol Deviation Report

The second bulk batch used near-equivalent reformulations rather than the exact frozen prompts for vr-05 through vr-08.
These outputs are preserved for auxiliary analysis but are excluded from the canonical 48-run visible set.

Source SHA-256: `4046c780a5685e48783cdb67417664026302e2450eaac089edc77f6e6e66f0bf`

| # | Case | Arm | Trial | Status | SHA-256 |
|---:|---|---|---:|---|---|
| 1 | vr-05-simplify-not-invent | baseline | 1 | deviation_imported | `4e9fef44e130fdcbfa27014563c099f222c7c4ae879056097cd5c66a836ace06` |
| 2 | vr-05-simplify-not-invent | baseline | 2 | deviation_imported | `965d61cea19c5225cebbdaa706642cc05092c2700c0f3e7198ccb7c2c76f4fde` |
| 3 | vr-05-simplify-not-invent | baseline | 3 | deviation_imported | `f8ea59d15cab7a4f5b234d79fcdcbbca9afe3284f3db7a60d425d30f15e8216b` |
| 4 | vr-05-simplify-not-invent | candidate | 1 | deviation_imported | `8ad3841bfdf843abfbc4c5b7f7255a75c03fe70a7ce1fb1ec1666fa328bd68c2` |
| 5 | vr-05-simplify-not-invent | candidate | 2 | deviation_imported | `0fb6985d2f1f828c417734c3d5c71721550b2b088d36dceeb9f5d0026f2cb0f0` |
| 6 | vr-05-simplify-not-invent | candidate | 3 | deviation_imported | `38e72269d0bbc83e774ab9df741fb9dd10d2b44459607a3536994c22d0357834` |
| 7 | vr-06-impossible-premise | baseline | 1 | deviation_imported | `60b516bf01d927dc8faa212317c8040962fad7e696784bb4f9b2d8ab4c46b767` |
| 8 | vr-06-impossible-premise | baseline | 2 | deviation_imported | `2a66c649a213f9958576454e5e02933760c8702417da9bdf1b57263f7a6b3ace` |
| 9 | vr-06-impossible-premise | baseline | 3 | deviation_imported | `a27e9cd0743980fff689008e5c89eb34c2e4fe729de4c0b239ac7b70e54f5d14` |
| 10 | vr-06-impossible-premise | candidate | 1 | deviation_imported | `d8f7280e5c40ccb6583ffb7dc49268df3bbb84befc6b541fb81b090c34435bb7` |
| 11 | vr-06-impossible-premise | candidate | 2 | deviation_imported | `c04fc825a57a0640e6e47ecb964f2cc03ac58dad3441845361f7acf7ebf2fb1a` |
| 12 | vr-06-impossible-premise | candidate | 3 | deviation_imported | `b2b312070c0225d80e329b8f6c9d9001adb5914d14be1ee6761f6beddbcb08d3` |
| 13 | vr-07-ai-wrapper-trap | baseline | 1 | deviation_imported | `84a698258cfce3200fbc02553bf666d25018771c9e2daaa4bebe80fdb79defdf` |
| 14 | vr-07-ai-wrapper-trap | baseline | 2 | deviation_imported | `549c71a190bc73ccae6e946bb657ffff72ad500052f81492ba507d053e3ad91a` |
| 15 | vr-07-ai-wrapper-trap | baseline | 3 | deviation_imported | `a1e6961d25a4a1a9416100eab93c6b7313d3267527a3189026313f7be4eaea9f` |
| 16 | vr-07-ai-wrapper-trap | candidate | 1 | deviation_imported | `0e773b808a0df0133c09273d6b0c4161a7f6e312c08165bce287d31c38596488` |
| 17 | vr-07-ai-wrapper-trap | candidate | 2 | deviation_imported | `d2465fcd937fcc4b12d512a6ac9d5b91f3b377c0e126d7a77d625a82990fbc45` |
| 18 | vr-07-ai-wrapper-trap | candidate | 3 | deviation_imported | `63115d19c4d6a0c150282cf37ef61afa0b67450e646f529f37f19f3986b37316` |
| 19 | vr-08-offline-clinic | baseline | 1 | deviation_imported | `f6bc95ccd62f2dce37bd29a868941f27ef6672006ff32228c331467fe73ce913` |
| 20 | vr-08-offline-clinic | baseline | 2 | deviation_imported | `5dee374e06a45a870983d6ec607d1345738bd5399d18560190f9f29cc03f002b` |
| 21 | vr-08-offline-clinic | baseline | 3 | deviation_imported | `82119c99d47c7e3a249ea618c650273ac0e2b9539ff6a293d09a2e613602e3a0` |
| 22 | vr-08-offline-clinic | candidate | 1 | deviation_imported | `b3c65ce89bf746a80df25f24c57a5cab989f811deecd4531295000355b4a0e2a` |
| 23 | vr-08-offline-clinic | candidate | 2 | deviation_imported | `9a2c961564c4bd7c4f5a1666217c0179cb44001b5155e4d220837d23a5288c6a` |
| 24 | vr-08-offline-clinic | candidate | 3 | deviation_imported | `c2e0dfb260e19ba2e89615c699f8f5349d4b27dcd8415ce5d583e9634bf1c126` |

## Canonical prompt rule

Only exact prompt strings from `benchmarks/visible-regression/cases.jsonl` count toward canonical completion.
