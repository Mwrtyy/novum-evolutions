Using the attached NOVUM methodology as the governing framework, the strongest candidate is a charge-neutral electro-acoustic reciprocity test: a low-energy screening method intended to flag latent failure precursors without cycling cells to failure.

1. Problem reframing

Challenge: detect cells likely to develop early failure—especially micro-shorts, delamination, abnormal gas generation, plating, or interfacial defects—using inexpensive, mostly non-destructive testing, while reducing reliance on long aging, CT inspection, cycle-to-failure, and destructive abuse tests.

This matters economically because wetting/formation can take 3–7 days and aging up to another two weeks; aging is partly used to reveal excessive leakage currents. Industrial self-discharge screening may require 10–30 days of rest.

The strongest baselines are therefore short electrical diagnostics such as resistance/relaxation measurements, longer self-discharge screening, ultrasonic inspection, and X-ray/CT for structural defects. Relaxation voltage can already reveal nascent internal shorts, while ultrasound is established as a non-invasive probe of internal mechanical state.

2. Frontier and opportunity gap

The frontier is crowded around single-domain measurements. Electrical methods include DC resistance, voltage relaxation and nonlinear impedance; acoustic methods measure transmission, time-of-flight, resonance or nonlinear harmonics; mechanical methods measure swelling/force; X-ray methods directly image internal geometry.

Ultrasonic resonance itself is particularly close prior art: acoustic resonances change strongly with SOC, and built-in piezoelectric transducers have been used to correlate natural frequency and damping with SOC/SOH. Acoustic hysteresis during cycling has also been reported as reflecting irreversible degradation.

The opportunity gap is therefore not ultrasound itself. It is using a deliberately reversible electrical perturbation to make the cell reveal whether its mechanical response is reversible.

3. Candidate portfolio

A mechanism-diverse pass produced 16 directions:

Mechanism	NOVUM gate
Charge-neutral electro-acoustic reciprocity	Survive
Bipolar micro-pulse thermal impulse asymmetry	Survive
Low-cost magnetic current-distribution mapping	Survive, hardware risk
Optical surface-strain reciprocity	Survive, packaging-sensitive
Nonlinear electrical impedance harmonics	Prior-art crowded
Voltage-relaxation leakage estimation	Known/strong baseline
Passive acoustic-emission counting	Known, weak specificity
Nonlinear ultrasonic pulse inversion	Prior-art collision
Static acoustic resonance drift	Prior-art collision
Swelling-force incremental analysis	Prior-art collision
RF dielectric reflectometry	Packaging limitation
Eddy-current edge/alignment inspection	Limited failure coverage
Resting microcalorimetry	Too slow/small signal
Pack differential resistance	Incremental
Acoustic gas/headspace resonance	Cell-format limited
PRBS electrical transfer-function anomaly	Incremental/model-sensitive

The important rejection is static ultrasound: patents and recent research already cover ultrasonic defect inspection, piezo-guided-wave health monitoring and formation-stage ultrasound.

4. Winning invention: CNEAR

Charge-Neutral Electro-Acoustic Reciprocity, or CNEAR, uses two inexpensive piezoelectric patches or clamp-on transducers plus the cell's existing formation-cycler connection.

At controlled SOC and temperature, establish an acoustic transfer-function fingerprint H
0
	​

(f). Apply a small positive current pulse transferring charge +q, interrogate two or three mechanically sensitive resonance bands, then apply an equal negative pulse −q, returning the cell to essentially its original SOC. Repeat with the order reversed: −q,+q.

Instead of asking whether ultrasound changed, calculate an order-dependent residual:

R=
∥H
0
	​

∥
∥(H
+−
	​

−H
0
	​

)−(H
−+
	​

−H
0
	​

)∥
	​


with voltage, delivered charge and temperature included as nuisance corrections.

Core mechanism

A healthy cell subjected to sufficiently small excursions should be approximately reversible: intercalation-induced stiffness/stress changes produced by +q should largely disappear when −q restores the initial electrochemical state.

A latent defect can violate that reciprocity. A micro-short continuously leaks charge; poorly bonded or delaminated interfaces can change contact under alternating electrochemical strain; localized plating/heterogeneity can have asymmetric kinetics; gas pockets can introduce nonlinear mechanical compliance. The defect therefore leaves a path-dependent acoustic residual after the net electrical perturbation is zero.

That creates the causal chain:

latent internal defect → asymmetric/local electrochemical strain or leakage → non-reciprocal acoustic transfer function → measurable residual R.

Electrochemical-mechanical coupling itself is well grounded: battery swelling tracks lithiation, ultrasonic properties change with electrochemical state, and present reviews explicitly identify linking wave physics to electrochemical changes as an important unresolved opportunity.

5. Innovation delta

Strip away the known pieces—piezo transducers, current pulses and ultrasound—and the irreducible difference is:

Use equal-and-opposite, near-zero-net-charge electrical perturbations in both temporal orders, and diagnose latent failure from the residual violation of electro-acoustic reversibility rather than from absolute impedance, voltage, acoustic amplitude, SOC or SOH.

I found close art for ultrasound during cycling, acoustic resonance/SOH monitoring, ultrasonic defect imaging, electrical nonlinear spectroscopy and relaxation-based short detection, but not a close disclosure in the searched material where pulse-order electro-acoustic reciprocity cancellation itself is the diagnostic variable. That supports a potentially differentiated mechanism, not a universal novelty claim.

6. Why it could cost less

The test can reuse the formation cycler's current-control and voltage channels. Incremental hardware is essentially piezo elements, a small pulser/receiver, ADC and temperature measurement rather than an imaging X-ray/CT system or laboratory impedance analyzer.

More importantly, the excitation can move only a tiny fraction of rated capacity and return that charge immediately, so screening need not consume meaningful cycle life. CT remains valuable for ground truth and special cases, but industrial CT requires specialized X-ray instrumentation and is sufficiently complex that high-speed production deployment remains an active engineering problem.

7. Evolution lineage

The first parent was simply ultrasound during a current pulse. That collided too strongly with existing guided-wave monitoring.

The first mutation made the electrical excitation charge-neutral, so ordinary SOC-dependent acoustic shifts largely cancel and the diagnostic imposes little net aging.

The second mutation performs the bipolar pulse in both orders and subtracts the two outcomes. That attacks fixture drift, ordinary reversible stiffness changes and static manufacturing variation, shifting the observable from “what does this cell sound like?” to “does this cell return by the same physical path?”

A further cost-reduction mutation would abandon full acoustic spectra after commissioning and monitor only two or three lot-specific resonant frequencies.

8. Decisive prototype

The smallest useful study would use production-equivalent pouch or prismatic cells, because acoustic coupling is easiest to control there.

Establish repeatability of R on healthy cells across repeated measurements, moderate SOC variation and the permitted temperature window.
Blindly test cells covering normal production variation plus independently identified defect-positive cells. Use CT, existing self-discharge screening and subsequent service/cycle history as ground truth; sacrifice only a small subset for teardown.
Compare CNEAR against simple DC pulse resistance and relaxation voltage using exactly the same cells. The invention only survives if the acoustic reciprocity term adds information beyond those cheaper electrical measurements.

Recent ultrasound work has demonstrated very high defect-classification accuracy under laboratory conditions, which makes the acoustic channel plausible, but also raises the bar: CNEAR must demonstrate an advantage specifically in early warning, test simplicity or reduced calibration, not merely show that ultrasound contains information.

9. What would falsify the core mechanism

The core claim is not merely “defective batteries produce different signals.” It is that latent failure mechanisms generate an abnormal electro-acoustic non-reversibility under charge-neutral perturbation.

I would kill that mechanism if a blinded study produced any of these results:

Primary falsifier: after matching SOC, temperature, chemistry and fixture pressure, defect-positive cells do not have a larger R than controls by at least two times the healthy-cell measurement standard deviation, and there is no monotonic increase of R with independently measured defect severity.

Specificity falsifier: the apparent R signal disappears after correcting for temperature and ordinary voltage relaxation, or an equivalent classifier using only voltage/current/temperature performs equally well. In that case the acoustic channel is redundant.

Mechanistic falsifier: deliberately reversing pulse order produces the same residual distribution in healthy and defective cells. That would directly contradict the proposed reciprocity-breaking mechanism.

Generality falsifier: R detects ordinary aging just as strongly as genuinely hazardous precursors and cannot separate them at matched capacity/SOH. It might remain an SOH technique, but the early-failure invention claim would fail.

For screening performance, I would use a deliberately demanding kill criterion: if the lower confidence bound of defect-detection AUROC does not exceed roughly 0.70, or it cannot outperform a simple relaxation/DC-resistance baseline at the same false-reject rate, it is not worth industrializing. Relaxation-based internal-short diagnostics are already strong enough that a more complicated sensor must clearly add information.

10. Verdict

Classification: potentially novel mechanism, evidence confidence currently low-to-moderate.

The supported pieces are that long aging/self-discharge screening is costly, ultrasound can sensitively detect mechanical/electrochemical changes, electrochemical swelling provides a physical coupling mechanism, and electrical relaxation can reveal internal shorts.

The speculative piece is the crucial one: that dangerous latent defects create a sufficiently large and sufficiently specific pulse-order electro-acoustic reciprocity violation before conventional diagnostics flag them. That is exactly the claim the proposed blinded test is designed to kill.

If that mechanism survives, CNEAR could become a cheap inline triage test that sends only suspicious cells to long aging, CT, or destructive validation—reducing destructive testing without pretending it can be eliminated altogether.
