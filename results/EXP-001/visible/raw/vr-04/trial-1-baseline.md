1. Problem reframing

Assume the target is manufacturing/commissioning screening of lithium-ion cells for latent early-life safety failures, especially metallic contamination, incipient dendrites, or weak internal micro-shorts.

The challenge is: detect cells likely to fail early using minutes of inexpensive, non-destructive measurement, outperforming long self-discharge screening while avoiding routine CT, teardown, or destructive abuse tests.

That is a meaningful bottleneck: production self-discharge screening can require roughly 10–30 days, while voltage-drop screening is already used to catch metallic contamination. The attached methodology calls for a precise causal mechanism with explicit evidence limits and a test capable of killing the central claim.

2. Frontier and opportunity gap

The obvious low-cost directions are already crowded. PRBS excitation can approximate impedance cheaply; ordinary pulse relaxation can recover EIS-like information; voltage relaxation has been used for plating and internal-short diagnosis; ultrasound can identify internal defects; and electrochemical noise has already been proposed as a battery-health signal.

A compact mechanism portfolio therefore looks like this:

Candidate mechanism	Main issue
Faster warm self-discharge screening	Mostly accelerates a known method
PRBS/cheap impedance	Strong prior art
Ordinary pulse-relaxation fingerprinting	Strong prior art
Mirrored charge/discharge asymmetry	Differentiated, but overlaps nonlinear impedance work
Thermistor lock-in for irreversible heating	Cheap, but likely weak signal
Piezo mechanical ring-down	Ultrasound/acoustic prior art is crowded
Passive electrochemical-noise screening	Promising, but noise is not deliberately coupled to the defect
Breathing-triggered telegraph spectroscopy	Uses a new causal probe: deliberately modulate unstable microcontacts, then listen for stochastic switching

The last one is the strongest candidate.

3. Invention: Breathing-Triggered Telegraph Screening

BTTS uses tiny, net-zero-charge current pulses to make the electrodes undergo microscopic reversible expansion/contraction—“breathing”—and then measures whether an incipient conductive bridge responds by repeatedly making and breaking electrical contact.

Lithiation is known to produce measurable electrode stress, so current excitation supplies a controllable mechanical perturbation without physically opening or abusing the cell. Separately, electrochemical voltage noise in Li-ion cells changes with aging, and recent work has specifically explored electrochemical noise as a way to identify lithium deposition.

The proposed causal chain is:

incipient metallic bridge or dendrite → mechanically marginal contact → current-induced electrode breathing changes contact resistance → bridge intermittently connects/disconnects → bursty, non-Gaussian terminal-voltage noise appears immediately after excitation.

The innovation delta is not the pulse, and not voltage-noise analysis individually. It is using controlled electrochemical strain as a defect modulator and detecting the pulse-locked stochastic conductance switching after the smooth electrochemical response has been removed.

4. Experimental architecture

A production formation cycler supplies the excitation. Add only a low-noise differential voltage front end/ADC and temperature measurement; no impedance analyzer, ultrasound array, X-ray system, calorimeter, or routine teardown is required.

At approximately 40–60% SOC and controlled temperature, first record perhaps 30–60 seconds of open-circuit voltage noise. Then apply a repeated bipolar sequence such as approximately +0.3–0.5 C for 1–2 s, rest, −0.3–0.5 C for the same duration, rest. Follow it with the mirrored sequence beginning with discharge. The exact current must stay comfortably inside the cell manufacturer's ordinary operating envelope. Net transferred charge over each complete sequence is approximately zero.

Sample voltage much faster than a normal production cycler—initially around 1–5 kHz is reasonable—and discard the immediate switching transient. For each pulse polarity, build a median smooth relaxation template from the repeated responses and subtract it.

What remains is the important quantity: the residual stochastic signal.

The screening statistic should emphasize step-like or burst-like events rather than average resistance. A practical Telegraph Excess Index can combine the number of residual voltage steps above, say, six times the pre-test robust noise level, their amplitudes/durations, excess kurtosis, and—crucially—the increase in event rate during the post-pulse window relative to the cell's own pre-pulse baseline.

This within-cell comparison is important: a noisy ADC or naturally higher impedance should not automatically make a cell defective.

5. Why it could reduce cost and destructive testing

Existing short pulse methods already show that useful electrochemical information can be obtained without full laboratory EIS hardware. BTTS goes after a different signal: intermittency of the suspected defect rather than its average impedance.

The initial destructive-validation campaign would use teardown/CT only on a stratified subset—high-BTTS cells plus matched low-BTTS controls. If the mechanism survives validation, production screening becomes electrical and non-destructive, with destructive analysis retained only for periodic audit and root-cause investigation.

It would not replace all destructive safety qualification. It is intended to reduce the number of cells sacrificed simply to discover which production cells contain latent micro-short-type defects.

6. The riskiest assumption

The weakest link is very specific:

An early micro-short or metallic/dendritic bridge must actually fluctuate enough under safe electrochemical breathing for its conductance changes to be visible at the external terminals.

There is evidence for the ingredients—electrode stress, electrochemical noise, and voltage-noise signatures associated with shorting—but I did not find direct evidence that safe bipolar pulses cause incipient microbridges to produce detectable random-telegraph switching. Voltage-noise methods have been used around later-stage short/thermal-runaway events, which supports detectability in principle but not the proposed early-stage mechanism.

7. What would falsify the core mechanism

The decisive test is a blinded cohort containing healthy cells, independently verified micro-short/metallic-contamination cells, and degraded/high-resistance cells without micro-shorts.

The mechanism is falsified if independently confirmed micro-short cells do not show a reproducible increase in pulse-locked step/burst activity relative to matched healthy controls after SOC, temperature, impedance, and instrumentation noise are controlled.

More specifically, it should be considered killed—not merely needing a better classifier—if the signal either (a) fails to distinguish verified microbridge cells from non-microshort cells, (b) does not change systematically when pulse amplitude changes the imposed electrochemical strain, or (c) can be reproduced with a passive R-C battery emulator plus a static shunt resistor. Those results would show that the observed “telegraph” signature comes from ordinary relaxation, electronics, or generic leakage rather than mechanically unstable internal contacts.

That is the important falsifier because it attacks the proposed causal mechanism, not merely predictive accuracy.

Verdict

Potentially novel mechanism; unverified. Electrochemical noise, bipolar pulses, pulse relaxation, nonlinear impedance, and voltage-noise short detection all have substantial prior art. In the searches performed, I did not find a close disclosure of deliberately using safe electrochemical breathing to modulate incipient conductive bridges and then measuring the pulse-locked stochastic switching residual. That is not proof of universal novelty, but it is sufficiently distinct—and cheaply falsifiable—to warrant testing before investing in a more elaborate diagnostic platform.
