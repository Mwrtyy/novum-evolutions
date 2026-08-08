Using the attached NOVUM methodology as the governing structure, the strongest candidate is a warm-loop thermal flywheel: direct-to-chip liquid cooling plus dry heat rejection, with thermal storage used specifically to bridge the hottest daily hours rather than consuming water or running a full chiller plant continuously.

1. Problem reframing

Achieve >90% reduction in operational freshwater consumed for cooling for a high-density AI data center in a hot climate, while maintaining hyperscale reliability and explicitly accounting for the added electricity, heat-rejection area, thermal-storage volume, maintenance burden, and extreme-weather failure modes.

Assume a representative 100 MW IT block, ambient design conditions around 45–47°C during summer peaks, and AI hardware capable of warm-water liquid cooling.

The strongest current baseline is no longer a conventional chilled-water/cooling-tower plant. ASHRAE now defines W45 liquid cooling up to 45°C inlet, while NVIDIA's current reference direction pairs such warm liquid loops with dry coolers; Microsoft is also deploying closed-loop designs that eliminate evaporative cooling water, while explicitly acknowledging an energy/PUE trade-off when mechanical cooling replaces evaporation.

The remaining problem is the hot-hour thermodynamic pinch: when outside air approaches or exceeds the required server-loop inlet temperature, a dry cooler either becomes enormous, loses useful capacity, or needs compressor assistance. DOE explicitly notes the underlying water-versus-electricity trade-off of dry versus evaporative heat rejection.

2. Frontier and opportunity gap

Saturated: cooling towers, adiabatic dry coolers, ordinary direct-to-chip liquid cooling, closed loops, air-cooled chillers and straightforward dry coolers. None is an invention by itself. Microsoft and NVIDIA are already moving toward near-zero cooling-water architectures.

Emerging: increasingly hot liquid loops. ASHRAE includes W45 and W+ classes; NVIDIA hardware documentation already shows components accepting 45°C liquid inlet and 55°C return, and its latest platform direction extends warm-liquid operation across more of the system.

Already explored but not exhausted: thermal storage combined with data-center free cooling. A 2025 study explicitly combines thermal storage and a water-side economizer, while older patents cover phase-change storage for data-center supplemental cooling. Thus, merely adding a tank or PCM is not defensibly novel.

Neglected design regime: size storage specifically around the few hours when dry-bulb temperature destroys the dry cooler's approach temperature, while allowing the dry cooler to continue rejecting whatever fraction of the load it still can. This changes storage from a full cooling plant substitute into a thermal peak clipper.

The central contradiction is therefore:

Freshwater ↓ → favor dry cooling
Hot-climate cooling electricity and equipment size ↓ → favor evaporation
Reliability ↑ → favor redundant chillers/towers
Land and complexity ↓ → avoid huge dry coolers/storage

The architecture has to move that trade-off rather than pretend it disappears.

3. Four mechanically distinct candidates
Candidate	Mechanism	Main price paid	Verdict
A. Diurnal thermal flywheel	W45 direct-to-chip + dry coolers + warm-temperature storage that absorbs only peak-hour residual heat and is recharged at night	Storage volume, controls, extra HX/pumps, dependence on nighttime temperature	Survives — strongest
B. Closed-loop borefield sink	Transfer liquid-loop heat into a large ground/borehole field, regenerating it with night dry cooling	Drilling, enormous geology-dependent field, long-term soil heating	Reject as primary hyperscale sink
C. Two-phase refrigerant path	Two-phase cold plates transport heat at high flux to dry condensers, using compression when ambient requires it	Refrigerant management, pressure equipment, service complexity, compressor power	Technically credible, weaker operational fit
D. Reclaimed-water/ZLD hybrid	Use municipal effluent or brackish water in evaporative rejection, heavily recycle blowdown and use dry trim	Still consumes water, treatment chemicals, scaling, blowdown infrastructure	Good freshwater substitute, not water-independent

Two-phase direct-to-chip equipment is already commercially emerging, so Candidate C is not a clean novelty claim. Google has likewise demonstrated reclaimed wastewater as a practical freshwater substitute, showing that Candidate D is proven in principle rather than novel.

4. Winning architecture: Warm-Loop Thermal Flywheel

The proposed architecture is:

AI racks
  │
  │  40–45°C liquid supply
  ▼
Direct-to-chip / fully liquid-cooled hardware
  │
  │  ~50–60°C return
  ▼
Redundant CDUs + plate heat exchangers
  │
  ▼
High-temperature facility loop
  │
  ├────────► Modular dry-cooler field ───────┐
  │                                           │
  ├────────► Stratified warm-water storage ──┤
  │                                           ├──► 40–45°C supply
  └────────► Latent-heat trim modules ───────┘
                       │
                emergency path
                       ▼
              air-cooled trim chiller

Normal operation

When ambient temperature provides sufficient approach, essentially the whole IT heat load goes directly to the dry-cooler field. No cooling water is evaporated.

This is consistent with the direction enabled by W45-class hardware; ASHRAE specifically notes that high-temperature secondary loops enable direct heat rejection to ambient air and that dry coolers require more physical footprint than cooling towers.

Hot afternoon

Suppose the racks require ≤45°C inlet water but ambient rises to 46°C. The dry coolers are not turned off. They continue rejecting as much heat as their actual derated performance permits.

If the 100 MW block produces roughly 100 MW of heat and the dry-cooler field can still reject 70 MW under that condition, storage absorbs only the 30 MW residual.

For a four-hour extreme period:

30 MW × 4 h = 120 MWh thermal storage.

That distinction is critical. A scheme attempting to store the entire 100 MW load for four hours would need 400 MWhₜₕ and quickly becomes land- and capital-heavy.

Storage architecture

Use two storage tiers.

The bulk tier is an ordinary stratified water tank operating over roughly a 10–15 K usable swing. At 120 MWhₜₕ, a 10 K water swing requires roughly 10,300 m³ of effective storage. That is physically plausible, but unmistakably large.

A second, smaller tier uses encapsulated PCM with a transition temperature close to the permissible facility supply temperature. Salt-hydrate PCMs are technically plausible in this temperature region and offer latent storage, but their cycling stability, phase separation, thermal conductivity and encapsulation life are genuine engineering risks rather than solved details.

The preferred design therefore uses cheap sensible storage for most capacity and PCM only as temperature trim, rather than betting the facility on thousands of tonnes of novel PCM.

Night recharge

After the daily ambient peak, the dry coolers reject:

the instantaneous AI heat load, and
additional heat from storage.

No refrigerator is needed to recharge storage whenever nighttime ambient is sufficiently below its charging temperature. Fans and pumps therefore replace most compressor work.

This is the causal advantage: time, rather than freshwater, is used to cross the hottest part of the climate envelope.

5. The trade-offs that remain
Dimension	Consequence
Freshwater	Cooling-loop evaporation can approach zero in normal operation. Makeup is principally initial fill, maintenance and abnormal draining rather than continuous evaporation.
Electricity	Dry-cooler fans and pumping consume more electricity than efficient evaporative rejection. Night recharge adds fan/pump runtime. Extreme conditions invoke compressor cooling.
Indirect water	Extra electricity can move water consumption upstream to electricity generation. This must be included in site accounting rather than declaring the system simply "water free."
Land	Dry coolers need more heat-exchanger surface than cooling towers, and thermal tanks/PCM modules add substantial footprint.
Capex	More HX surface, thermal storage, valves, controls and redundant piping than a straightforward tower system.
Maintenance	More fan motors, isolation valves, storage instrumentation and heat-exchanger surfaces; PCM adds a new aging mechanism. Coolant chemistry and commissioning/disposal remain operational issues.
Reliability	Storage has finite duration. A multi-day heat wave can exhaust it, so it cannot be the sole ultimate heat sink.
Noise	A large dry-cooler array can create significant fan noise, particularly during night recharge.
Climate dependence	Weak in climates with little diurnal temperature swing. Hot nights can eliminate the free-recharge window.

The indirect-water point is significant. LBNL estimated an average 4.52 L/kWh indirect water consumption associated with U.S. data-center electricity in 2023, although the actual value varies dramatically with generation mix. A cooling architecture that saves local water by materially increasing power consumption can therefore shift rather than eliminate water impact.

Google likewise states that water cooling can use roughly 10% less energy than air-based cooling in suitable situations, illustrating why eliminating evaporation is not environmentally free.

6. Reliability architecture

Thermal storage should not be credited as indefinite cooling redundancy.

Use:

N+1 or N+2 dry-cooler cells so individual fans/coils can be isolated.
Redundant pumps and CDU paths.
Multiple independently isolatable storage modules rather than one monolithic PCM vessel.
Continuous storage state-of-charge estimation from temperatures and flow/energy balances.
An air-cooled mechanical trim plant, perhaps only a fraction of full site load, sized against the statistically credible combination of high ambient temperature and depleted storage.
A final compute-power derating mode for noncritical workloads if both storage and trim cooling lose margin.

The emergency mechanical path is deliberately air cooled, not evaporative. Freshwater therefore does not become an invisible reliability dependency.

7. Red-team and rejected ledger

“Just build bigger dry coolers.” Rejected as the universal answer. It is simpler, and should win wherever sufficient land and approach temperature make it economical. The thermal flywheel only earns its complexity when extreme-hour dry-cooler overbuild is materially more expensive than storage.

“Use underground cooling.” Rejected for the base architecture. A 100 MW continuously operating heat source is enormous on geothermal scales; ground thermal saturation, drilling expense and site geology become first-order uncertainties.

“Replace everything with PCM.” Rejected. PCM storage in data centers is already prior art, and material cycling/power density make an all-PCM design needlessly dependent on a weak assumption.

“Use reclaimed water and call it solved.” Constrained. This can dramatically reduce freshwater demand and may be preferable where wastewater infrastructure already exists, but the facility remains dependent on a large consumptive water stream plus treatment and discharge infrastructure. Google demonstrates that this approach is operationally real.

8. Evolution lineage

Generation 1: W45 loop + dry cooler + full PCM storage.

Weakness: unnecessarily large PCM inventory and materials-life risk.

Generation 2: replace most PCM with low-cost stratified sensible storage; retain PCM only across the narrow temperature range where staying below the IT inlet limit matters.

Gain: less specialty material and easier inspection/replacement.

New weakness: substantially larger storage volume.

Generation 3 — selected: keep hybrid storage, allow dry coolers to reject partial load continuously during peak conditions, and add a small air-cooled mechanical residual path instead of sizing storage for the worst imaginable heat wave.

This is the key architectural mutation: storage is sized against the statistical residual after peak dry cooling, not against total data-center heat output.

9. Decisive engineering gate

Build a roughly 0.5–2 MW thermal pilot consisting of a representative CDU/facility loop, one dry-cooler bank and one modular storage train.

Feed it a measured hot-climate hourly weather profile and reproduce the intended 40–45°C supply and 50–60°C return conditions.

The candidate survives if it can simultaneously demonstrate:

cooling-loop freshwater consumption <0.02 L/kWh IT equivalent;
uninterrupted compliance with the hardware inlet-temperature limit;
full overnight storage recovery on the design sequence;
no reliance on evaporative heat rejection;
acceptable auxiliary electricity relative to the reference hybrid cooling plant; and
graceful transition to mechanical trim when storage is depleted.

Kill or materially redesign it if the storage cannot recharge across realistic consecutive hot days, if dry-cooler derating makes the residual load much larger than assumed, or if maintaining the thermal-storage system costs more in land/energy/availability than simply overbuilding dry coolers plus a conventional air-cooled trim plant.

10. Verdict

Classification: Differentiated architecture, not a defensible claim of a novel fundamental cooling mechanism.

What is well supported is that warm-water AI hardware can enable dry heat rejection; closed loops can eliminate routine evaporative cooling water; dry cooling has real energy and footprint costs; and thermal storage can shift cooling duty in time.

The inventive hypothesis is narrower: using hybrid warm-temperature storage to absorb only the residual heat left when a W45 dry-cooling system hits its hottest-hour thermodynamic pinch can produce a better water–energy–land compromise than either full evaporative cooling or brute-force dry-cooler/chiller overbuild.

The two most uncertain quantities are the actual dry-cooler derating curve at 44–48°C ambient and the number/duration of consecutive nights that can fully recharge storage. Those two parameters determine whether this architecture is an economical improvement or merely extra machinery.

The largest remaining prior-art region is hyperscaler and cooling-vendor patents covering combinations of W45/W+ loops, dry coolers, latent/sensible storage and predictive control. The search already finds close thermal-storage and dry-cooling art, so the appropriate novelty claim remains differentiated/unverified, not “first” or “patentable.”