Using the uploaded NOVUM standard, I’m treating the invention as a mechanism that must be materially different, operationally plausible, and decisively falsifiable—not merely a cheaper sensor bundle.

Invention candidate: Electro-Acoustic Intermodulation Screening

Goal: detect cells beginning to develop mechanically coupled failure precursors—delamination, gas pockets, contact loss, abnormal plating-induced stress—without repeatedly sacrificing cells for teardown.

The key change is to measure how a cell's mechanical resonance changes in synchrony with a tiny electrochemical perturbation.

Existing approaches already use ordinary ultrasound, nonlinear acoustic resonance, guided waves, EIS, and combinations of ultrasound plus EIS. Ultrasound can track structural and SOC-dependent changes, while EIS can detect early internal shorts; nonlinear acoustic battery diagnostics are also already patented.

The irreducible difference here is:

Do not classify the acoustic spectrum itself. Measure the cross-transfer function from a small reversible electrical perturbation to the cell's mechanical impedance.

How it works

Attach or spring-clamp a single inexpensive PZT patch to the cell. The patch serves simultaneously as actuator and mechanical-impedance sensor.

At a controlled SOC:

Apply a very small, zero-net-charge sinusoidal current perturbation to the battery, for example roughly C/100–C/20 at 0.02–0.2 Hz. This periodically perturbs lithiation without doing a meaningful charge/discharge cycle.
Simultaneously excite the PZT near one of the cell/PZT mechanical resonances, perhaps in the tens-to-hundreds-of-kHz range.
Measure PZT admittance and synchronously demodulate its resonance frequency, amplitude and damping at the electrical modulation frequency.

Call the main quantity the electromechanical modulation coefficient:

M
f
	​

=
Δq
Δf
r
	​

	​


with analogous coefficients for resonance damping Q
−1
 and phase.

Lithium insertion/removal inherently couples ion motion to strain, while battery ultrasound is already known to respond to electrode mechanical properties and internal interfaces.

The hypothesis is that an intact stack responds relatively smoothly and reversibly. An incipient gas pocket, partial delamination or mechanically heterogeneous degradation changes contact stiffness locally, causing the electrochemically driven strain to produce an abnormally large, nonlinear, phase-lagged, or hysteretic modulation of mechanical impedance.

That cross-modal response is the diagnostic—not absolute ultrasound amplitude.

Why it could be substantially cheaper

The instrument can consist of a PZT patch, low-voltage waveform source, transimpedance/sense circuit, ADC and the current-control capability of an ordinary battery cycler. It avoids CT/X-ray imaging, precision scanning ultrasound arrays and a dedicated broadband electrochemical impedance analyzer.

It also has an important statistical advantage over teardown: every cell can be measured repeatedly throughout life. Destructive characterization becomes validation sampling rather than the primary measurement.

A practical study could destructively analyze only a stratified subset—for example cells with high, medium and low modulation scores plus randomly selected blind controls—while preserving most of the cohort for longitudinal observation.

Why static ultrasound alone is not enough

Static acoustic signatures strongly depend on SOC, temperature, clamping, geometry and cell construction; conventional ultrasound therefore has a difficult nuisance-variable problem.

Here, synchronous detection asks a narrower question:

“What part of the mechanical response moves at exactly the frequency and phase imposed electrochemically?”

Static fixture variation largely drops out. Joule heating provides an additional check: its dominant quadratic contribution occurs at DC/approximately twice the electrical excitation frequency, whereas reversible electrochemical coupling can be examined at the fundamental.

Decisive falsification

The core mechanism is:

Incipient failure-associated mechanical heterogeneity measurably alters the mechanically observed response to reversible electrochemical strain before gross cell failure.

I would pre-register the following kill test.

Take healthy cells and cells independently verified to contain early mechanically relevant defects, while matching SOC, temperature, cell design and clamp force. Perform the new measurement blindly. Use CT or post-mortem analysis on only the validation subset to establish the actual defect state.

Falsify the mechanism if both of these occur in two independent cell batches:

confirmed early-defect cells exhibit essentially the same normalized electro-acoustic modulation coefficient, phase lag and hysteresis as healthy controls—e.g. standardized separation <0.5 SD with no monotonic relationship to independently measured defect severity; and
ordinary acoustic/EIS or physical examination confirms that the targeted defects really were present and detectable, ruling out “the cells simply had no defect” as an explanation.

An even stronger mechanistic falsifier would be finding that the apparent modulation follows temperature or clamp-pressure modulation equally well in an electrochemically inert dummy stack, and vanishes after those confounds are controlled. That would show the signal is a fixture/thermal artifact rather than electrochemical-strain coupling.

If those observations occur, the central causal idea should be killed rather than rescued with a more elaborate classifier.

Boundary conditions

This method should not be claimed as a universal battery-failure detector. Its strongest plausible domain is failure modes that alter mechanical coupling or local strain transfer. A purely chemical degradation pathway that changes capacity without appreciably changing stiffness, contact or swelling may remain invisible.

My search found substantial prior art around ultrasonic SOH monitoring, acoustic resonances, nonlinear resonant ultrasound, built-in PZT guided waves, and combined acoustic/EIS diagnostics. I did not find a close match in the searched material for using a low-frequency electrochemical perturbation specifically to gate a PZT mechanical-impedance resonance and using the resulting cross-modulation coefficient as the early-failure observable. The appropriate NOVUM verdict is therefore potentially novel mechanism, not established novelty.
