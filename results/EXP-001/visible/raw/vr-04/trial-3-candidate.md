Using the uploaded NOVUM methodology as the governing framework, the strongest candidate is a low-cost electromechanical null test for lithium-ion pouch cells.

1. Problem reframing

Achieve early identification of cells likely to fail prematurely using equipment inexpensive enough for broad screening, while reducing reliance on teardown, abuse testing, CT, or long-duration life tests.

The strongest practical baselines are electrical self-discharge/voltage-drop screening, EIS, ultrasound, thermal imaging, and—in higher-budget settings—X-ray/CT. Self-discharge screening can be slow because electrochemical relaxation contaminates the measurement; ultrasound and magnetic imaging provide richer internal information but require additional instrumentation.

The key contradiction is therefore:

Cheap measurements are usually spatially/mechanistically weak; mechanistically rich measurements are usually slower or more instrument-intensive.

2. Frontier and opportunity gap

Mechanical deformation is promising because lithium intercalation itself changes electrode dimensions. Surface-mounted strain gauges have already demonstrated measurable cell deformation during charge/discharge, including with very inexpensive HX711/Arduino-class readout hardware. Strain features have also been associated with battery health.

But simply measuring swelling is not sufficiently differentiated. Strain-based battery testing already has substantial prior art, as do piezoelectric ultrasonic monitoring and bipolar electrical pulse characterization.

A particularly important collision appeared in the current frontier: a June 2026 preprint explicitly proposes small harmonic current excitation with measurement of stack stress as mechano-electrochemical impedance spectroscopy. That kills the simpler idea of claiming current→stress spectroscopy itself as the invention.

The remaining gap is not measuring strain—it is using strain as a physical null test for irreversibility.

3. Invention: Electromechanical Reciprocity Echo

ERE — Electromechanical Reciprocity Echo uses two equal-and-opposite, low-stress current pulses around the same SOC and asks whether the cell mechanically returns along the mirror image of its first trajectory.

A healthy cell near a fixed operating point should exhibit largely reversible intercalation-induced deformation: a small positive charge excursion and an equal negative excursion should approximately undo each other's chemo-mechanical effect. A developing defect can break that reciprocity through heterogeneous ion transport, interfacial slippage, delamination, abnormal gas production, parasitic charge consumption, micro-short leakage, or irreversible mechanical rearrangement.

The diagnostic signal is therefore what fails to cancel, rather than absolute swelling.

Operating principle

Place a pouch cell between two smooth plates under a small reproducible preload. One plate sits on an ordinary miniature load cell; alternatively, use a bonded foil strain gauge. Add one surface thermistor. Existing battery-cycler channels provide the electrical stimulus.

At approximately 40–60% SOC:

Rest the cell until short-term drift is stable.
Apply a modest +I pulse—for example roughly 0.2–0.5 C for tens of seconds.
Rest briefly and record force relaxation.
Apply the same integrated charge with opposite sign, −I.
Continue recording until the mechanical response settles.
Repeat once with the pulse order reversed.

The net SOC displacement is close to zero, so the test consumes very little cycle life.

Instead of asking whether force changed, calculate a reciprocity residual:

R(t)=F
+
	​

(t)+F
−
mirror
	​

(t)

after correcting for temperature, baseline drift, and fixture creep.

For an ideally reversible local response, the two mechanical trajectories cancel and R approaches zero. The useful features are the integrated residual, post-pair force offset, relaxation-time mismatch, and positive-versus-negative pulse gain asymmetry.

A second channel retains the ordinary antisymmetric response. That catches defects that change mechanical gain or transport time without producing strong irreversibility.

4. Why this could be cheaper

The irreducible hardware addition is a load cell or foil gauge, a high-resolution bridge ADC, a thermistor, and a simple compression fixture. A recent experimental study demonstrated Li-ion pouch deformation measurement using a 120 Ω foil gauge, an HX711 module and Arduino-class electronics, supporting the feasibility of very inexpensive mechanical readout.

ERE does not require an ultrasound pulser/receiver, scanning stage, IR camera, magnetic-field sensor array, potentiostat-grade EIS front end, or X-ray equipment.

The main cost caveat is that it assumes a battery cycler is already present. Thus the strongest claim is low incremental instrumentation cost, not universally low laboratory cost.

5. Mechanism-diverse portfolio

I screened 18 mechanism families and retained four materially different ones:

Candidate	Mechanism	Main verdict
ERE	Detect non-cancellation of matched electrochemical strain trajectories	Winner — differentiated architecture
Sparse Hall pulse gradiometry	Two/four cheap magnetic sensors detect abnormal current redistribution	Feasible but strongly adjacent to established magnetic-field imaging
Thermal parity screening	Separate odd/even thermal response under ± current modulation	Too close to established lock-in thermography
Accelerated relaxation screening	Use short pulse/rest transients instead of long self-discharge storage	Cheap, but voltage-relaxation and bipolar-pulse spaces are already crowded

The important evolution was linear current→stress spectroscopy → reciprocity-breaking mechanical null test. The former collided directly with recent mechano-electrochemical impedance work; the latter deliberately interrogates nonlinear/non-returning behavior instead.

6. Assumption graph

The causal chain is:

incipient defect
→ altered ion redistribution / parasitic reaction / mechanical accommodation
→ positive and negative charge perturbations cease being mechanical mirror images
→ measurable non-zero reciprocity echo
→ suspect cells can be selected for expensive inspection before conventional capacity loss becomes obvious.

The weakest assumption is the middle one: that important early-failure mechanisms generate a reciprocity-breaking mechanical signature large enough to exceed cell-to-cell variation, temperature effects and fixture creep.

That is the assumption the first validation must attack.

Static strain alone is particularly vulnerable to SOC and temperature confounding. Rest-period strain is also known to relax through lithium redistribution and viscoelastic processes, so temperature and timing must be tightly controlled.

7. Smallest useful prototype

Use approximately 24–40 nominally identical pouch cells and one reusable fixture. Run ERE at the same SOC, temperature and preload on every cell.

Ground truth should come primarily from subsequent ordinary cycling, self-discharge behavior, ultrasound or CT where available. Only a small strategically selected subset needs destructive teardown: the strongest ERE positives, strongest negatives, and discordant cases.

That creates a practical destructive-testing strategy: screen everything cheaply, destructively inspect only information-rich tails of the distribution plus random controls.

For production screening, the fixture can eventually become a spring-loaded nest with a single load cell rather than permanently attaching a strain gauge to every cell.

8. Decisive falsification

The central mechanism is:

Cells heading toward premature failure develop an abnormal, non-reciprocal chemo-mechanical response to matched positive and negative micro-charge perturbations before conventional gross degradation is apparent.

The mechanism should be considered falsified if, in a blinded prospective cohort:

cells subsequently confirmed to have early internal defects or premature degradation show ERE residuals statistically indistinguishable from matched healthy cells before failure, after controlling SOC, temperature and fixture preload.

An especially strong falsification would be finding that the apparent ERE residual is reproduced equally well by an inert mechanical/thermal dummy, or that thermistor measurements plus fixture creep fully explain it. In that case the supposed electro-chemo-mechanical defect signal is an instrumentation artifact.

I would set an early kill threshold rather than optimize indefinitely: if the mechanical features cannot outperform a temperature-only/drift-only null model and cannot separate future-failing from healthy cells materially better than chance across at least two distinct failure mechanisms, abandon ERE.

9. Evidence status and verdict

Supported: intercalation generates externally measurable strain; inexpensive strain instrumentation works; mechanical relaxation contains information about internal lithium redistribution; strain features change with degradation.

Inferred: incipient defects should perturb the symmetry and return-to-origin behavior of that mechanical response.

Speculative: the reciprocity residual will become abnormal sufficiently early, consistently, and across enough defect classes to outperform cheap electrical screening.

Prior-art verdict: Differentiated architecture / potentially novel mechanism, not verified as universally novel. The searches found strain-based SOH diagnostics, externally excited acoustic sensing, bipolar voltage interrogation, and linear current-to-stress spectroscopy, but not a close match to using matched bipolar electrochemical excitation specifically as a mechanical reciprocity/null test for early-failure screening. The largest remaining prior-art risk is battery diagnostic patent literature combining strain sensing with custom pulse sequences.

The candidate is worth validating because its riskiest assumption is cheap to kill: a reusable clamp, load-cell electronics, thermistor, and existing cycler can determine whether the reciprocity signal exists before investing in a larger destructive-testing program.
