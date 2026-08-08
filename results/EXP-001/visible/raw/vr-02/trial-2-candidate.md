I used the attached NOVUM instructions as the governing methodology for this run.

1. Problem reframing

Challenge: Achieve near-zero operational freshwater consumption for cooling a high-density AI facility in a hot climate, while maintaining full-load compute availability and explicitly accounting for added electricity, heat-rejection area, storage volume, maintenance burden, and failure modes.

I will use a 100 MW IT-load facility as the reference case, with a hot-climate design condition around 45–46°C daytime dry-bulb and materially cooler nights. The strongest practical baseline is warm-water direct-to-chip cooling with dry coolers. ASHRAE now identifies W45 and W+ liquid-cooling classes and describes 45°C-supply architectures capable of direct dry heat rejection; however, it also notes that extreme ambient temperatures can force throttling or require adiabatic assistance.

The core contradiction is therefore not “water versus liquid cooling.” It is:

Evaporation cheaply creates a cold heat sink during the hottest hours; eliminating evaporation means paying instead in temperature headroom, fan power, exchanger area, thermal storage, mechanical refrigeration, or reduced compute.

Microsoft makes this trade explicitly: its zero-water-evaporation design recirculates coolant in closed loops, but replacing evaporative cooling increases PUE somewhat despite warmer liquid temperatures mitigating the penalty.

2. Frontier and opportunity gap

The relevant frontier has four regions.

Saturated: cooling towers, adiabatic fluid coolers, conventional chillers, ordinary direct-to-chip liquid loops, and plain dry coolers. Dry mode eliminates evaporation but increases fan energy and heat-exchanger requirements; wet/adiabatic operation reduces footprint or fan power by spending water.

Emerging: W45/W+ AI hardware, very-high-temperature liquid loops, Cold Underground Thermal Energy Storage, and increasingly sophisticated liquid-loop control. DOE/NREL is explicitly investigating Cold-UTES for data centers as a non-water-consumptive way of shifting cooling demand.

Site-specific alternatives: deep seawater cooling can be attractive in tropical coastal locations, but it substitutes marine infrastructure, pumping, biofouling, corrosion, permitting, and ecological constraints for freshwater use.

Opportunity gap: most designs attack hot weather by making the heat sink colder—evaporation or refrigeration. A better fit for water-constrained AI is to make heat rejection partially time-shiftable, exploiting the fact that an AI rack can continuously generate heat while the facility need not reject every joule to outdoor air at exactly the instant it is generated.

3. Assumption graph

The critical chain is:

45°C-compatible AI hardware → high return-water temperature → dry heat rejection through most hours → temporary storage of the hot-hour rejection deficit → nighttime rejection of that stored heat.

For 100 MW of heat and a nominal 45°C supply / 60°C return, a 15 K liquid temperature rise requires roughly 1,595 kg/s, or about 5,740 m³/h of circulating water equivalent. This argues for several parallel thermal trains rather than one enormous loop.

The weakest assumption is hardware temperature compatibility. If the selected GPU, networking, memory, power electronics, or storage stack actually requires W32 rather than approximately W45 facility water, the hot-climate advantage collapses. ASHRAE's W45/W+ classes show that such higher-temperature operation is becoming legitimate, but it is not safe to assume every deployed AI platform supports it.

4. Four mechanically distinct candidates
Candidate	Mechanism	Main benefit	Main price paid	Verdict
A. WarmLoop Dry	45°C D2C loop directly feeding oversized dry coolers	Simplest near-zero-water design	Large cooler field, peak fan energy, poor extreme-heat margin	Known/common
B. WarmShift	Warm D2C + dry coolers + moderate-temperature thermal storage that shifts only the hot-hour rejection deficit	Near-zero freshwater without designing everything around the worst hour	Tanks/storage, controls, extra pumps, finite ride-through	Survivor
C. Cold-UTES Spine	Store cooling underground and dispatch it during hot/grid-peak periods	Low water and potentially lower peak electricity	Geology, drilling, subsurface permitting, thermal saturation	Emerging/site-dependent
D. Deep-Seawater Sink	Secondary seawater circuit rejects heat through titanium/high-alloy exchangers	Excellent hot-climate sink with negligible freshwater	Coastal siting, long pipes, pumps, fouling, corrosion, ecological permitting	Strong but location-bound

Candidate C has credible current R&D support: NREL describes Cold-UTES specifically as reducing dependence on energy- or water-intensive data-center cooling. Candidate D likewise has sound thermodynamics, but the requirement for suitable coastal bathymetry makes it a siting strategy rather than a generally deployable architecture.

5. Winning architecture: WarmShift
Operating principle

Use warm-water direct-to-chip cooling as the continuous heat-collection mechanism, dry air as the normal ultimate heat sink, and a sealed thermal buffer as a temporal decoupler between compute heat generation and outdoor heat rejection.

The buffer does not try to store all data-center heat. It only stores the fraction that the dry coolers cannot economically reject during the hottest few hours.

Reference architecture for 100 MW IT

Rack/TCS layer: Four independently isolatable ~25 MW rack-cooling zones. Each zone has redundant CDUs, pumps, leak detection, pressure sensing, and plate heat exchangers. Nominal operating target: approximately 45°C supply / 60°C return, subject to the selected hardware envelope.

Facility loop: A closed, chemically managed facility-water loop. The technology coolant and facility water remain separated at CDUs so that rack-side water chemistry is not dictated by the outdoor plant.

Dry heat-rejection plant: Roughly 120 MWth nominal modular dry-cooler capacity, divided among many independently isolatable cells rather than a single bank. Exact rating must come from hourly climate/vendor curves; the goal is not 120 MW at the absolute annual maximum temperature, but full rejection during ordinary hot conditions plus recharge capacity at night.

ASHRAE describes essentially this warm-water/dry-cooler pathway and notes that closed-loop dry rejection can achieve virtually zero cooling water consumption, at the expense of greater footprint and weather sensitivity.

Thermal buffer

Suppose the dry plant is deliberately allowed to fall 20 MWth short for six extreme daytime hours.

Including 25% reserve:

20 MW × 6 h × 1.25 = 150 MWhth.

A simple, maintainable implementation is about 16,000 m³ of stratified thermal storage operated over roughly a 10 K useful temperature band. Four ~4,000 m³ tanks would allow isolation and maintenance without taking out the whole buffer.

The tanks should preferably be filled with treated reclaimed/non-potable water and remain sealed. Their water is inventory, not an evaporative consumable.

During cool nighttime conditions, the dry coolers charge the lower-temperature layer. During the hottest hours, stored coolant is blended through a heat exchanger to keep rack-supply temperature within its limit while the outdoor plant rejects whatever it can.

Phase-change storage can reduce volume, but it is not my preferred first implementation. Data-center PCM storage is already established prior art—including patents for deferred heat management—while large-scale PCM introduces material aging, thermal-conductivity, supercooling/segregation, enclosure, inspection, and replacement issues. The simpler stratified-water substitute wins unless land is exceptionally expensive.

Extreme-condition trim

Install approximately 20–30 MWth of air-cooled mechanical trim, modularized, not a 100 MW conventional chiller plant.

Its purposes are limited:

nights too hot to recharge the buffer;
multi-day heat waves;
simultaneous dry-cooler maintenance and extreme weather;
abnormal IT temperature limits.

This is the important honesty point: WarmShift does not claim that a 50°C heat wave can always be handled passively. When ambient conditions eliminate the required temperature difference, electricity replaces water.

A representative 20 MWth trim load at a COP of 4 would add about 5 MW electrical while running. Actual COP must be obtained from the selected chiller at the project's unusually high leaving-water temperature and design ambient.

6. What the architecture actually trades
Freshwater

Routine cooling evaporation and cooling-tower blowdown disappear. Makeup is principally leaks, maintenance drains, and occasional cleaning rather than continuous evaporation.

That distinction is significant: Microsoft's current zero-evaporation architecture likewise uses closed-loop chip cooling and reports near-zero cooling WUE for such facilities, while explicitly retaining water for non-cooling building uses.

There is still water inventory. A 16,000 m³ buffer is substantial. Using reclaimed water avoids converting “zero consumption” into a hidden one-time potable-water demand.

Electricity

Dry cooling requires moving enormous quantities of air. For a rough first-principles illustration, rejecting 100 MW while allowing outdoor air to warm 15 K requires roughly 6,600 kg/s of air, or around 5,500 m³/s.

At realistic coil/fan pressure losses that implies megawatts, not kilowatts, of fan power. Pumps add further load. A plausible conceptual cooling-auxiliary range is several percent of IT power, with mechanical trim adding several additional megawatts during extreme conditions.

That is consistent with the broader dry-cooled AI design envelope ASHRAE discusses, roughly PUE 1.05–1.15 for highly integrated warm-liquid facilities rather than a fiction of PUE = 1.00.

Land

At a 2.5–3 m/s coil-face velocity, the same approximate airflow implies on the order of 2,000 m² of net coil face before accounting for V-bank arrangement, N+1 redundancy, recirculation separation, access aisles, acoustic treatment, and service clearances.

Consequently, a 100 MW dry-cooler installation should be thought of as an order-of-hectares mechanical yard, not a rooftop accessory. ASHRAE explicitly flags the larger footprint of dry rejection versus evaporative towers.

The storage plant adds roughly another fraction of a hectare to hectare once tank spacing, bunding, piping and service access are included.

Maintenance

Water treatment becomes easier because there is no open tower, but other maintenance increases:

fin fouling from dust/sand;
coil washing;
EC fan/motor replacement;
corrosion inspection;
thousands of valves and connections in liquid-cooled racks;
CDU filters and plate-HX cleaning;
tank stratification instrumentation;
leak detection;
periodic water-chemistry control;
air-cooled chiller compressor/refrigerant service.

A dusty desert site may therefore save enormous quantities of water while creating a coil-cleaning and fan-maintenance problem.

Reliability

The thermal store improves resilience against short heat-rejection disturbances but creates no energy from nowhere.

I would partition the system into four ~25 MW thermal zones, use numerous independently isolatable dry-cooler cells, redundant pumps/CDUs, four separate storage tanks, and several independent trim-chiller modules.

The dispatch hierarchy should be deterministic and fail-safe:

dry rejection → charge storage whenever surplus exists → discharge storage during peak ambient → mechanical trim → controlled derating of deferrable training jobs.

No opaque “AI optimizer” is required. Forecast-aware model-predictive control is useful, but conventional safety interlocks remain authoritative.

7. Red-team and rejected directions

Pure dry cooling with no buffer or trim: rejected. Above the dry-cooler temperature limit, ASHRAE itself identifies thermal throttling or another cooling mechanism as necessary.

Potable-water adiabatic backup: rejected as a default because it merely hides freshwater use in the few hours when community water systems are often under maximum stress. ASHRAE confirms that adiabatic precooling buys lower fan power/smaller equipment precisely by evaporating water. Reclaimed-water adiabatic trim could be an optional site-specific substitute for some chiller electricity.

Radiative-sky cooling as the primary sink: rejected for scale. A Dubai experimental system measured roughly 30–45 W/m² average nighttime cooling power. At that flux, an instantaneous 100 MW sink alone corresponds to roughly 2.2–3.3 km² of active radiator area, before duty-cycle and storage losses. It can be an auxiliary surface, not the backbone of a hyperscale facility.

Immersion as the water-saving mechanism: unnecessary. Immersion can improve chip heat transfer, but it does not eliminate the need for an ultimate heat sink; it also materially changes hardware servicing, fluid compatibility and operational practices. Direct-to-chip is the simpler mechanism for the particular water objective.

8. Evolution lineage

The initial survivor combined warm-water D2C, dry coolers and PCM storage.

The first simplification removes the PCM and substitutes stratified sealed water storage, accepting more tank volume in exchange for easier condition monitoring, mature heat exchangers, straightforward replacement chemistry, and lower material uncertainty.

The second change adds limited air-cooled mechanical trim rather than further enlarging the thermal store. That fixes the fatal multi-day-heatwave case. A finite tank cannot solve a prolonged period in which nighttime ambient remains too hot to recharge; refrigeration can, but the energy penalty is exposed rather than concealed.

The resulting architecture is therefore not the theoretically lowest-water system at any cost. It is the one with the best balance of water independence, deployability and graceful failure.

9. Falsification gate

Before committing a campus, build one approximately 1 MW thermal train with production-representative racks, CDU, dry cooler, stratified buffer and trim cooler.

The architecture fails its central claim if, under a representative multi-day extreme-weather profile, any of these occur:

production hardware cannot sustain full compute at the intended warm-water inlet;
the buffer cannot recover sufficient state of charge overnight;
cooling auxiliary power repeatedly exceeds roughly 10% of IT load to maintain the thermal envelope;
a single ordinary cooling component failure causes rack thermal throttling rather than isolation/failover;
routine cooling requires continuing freshwater makeup beyond leakage/maintenance quantities.

The most important measurement is not headline PUE. It is the joint hourly curve of IT power, cooling electricity, outdoor dry/wet-bulb temperature, storage state of charge, rack temperature margin, and cooling-water makeup.

10. Decision and uncertainty
Dimension, 0–10	A: Pure dry	B: WarmShift	C: Cold-UTES	D: Deep seawater
Mechanism novelty	2	5	5	3
Problem value	9	9	9	9
Advantage magnitude	7	8	8	9
Technical feasibility	9	8	6	7
Adoption feasibility	8	7	4	3
Testability	9	9	5	6
Defensibility	3	5	5	4
Evidence confidence	9	7	5	7
Fatal-risk severity, 10 worst	5	4	7	7

The scores most likely to move are WarmShift technical feasibility, because it depends heavily on the selected rack's true coolant-temperature envelope, and advantage magnitude, because site-specific hourly weather determines whether the thermal buffer is used for tens or hundreds of hours per year.

Honest verdict

WarmShift is a differentiated architecture, not a defensible claim of a new fundamental cooling mechanism. Warm-water D2C, dry coolers and thermal storage all have substantial prior art; data-center PCM storage in particular predates this proposal.

Its irreducible innovation delta is narrower: size the dry plant for economically common hot conditions, then treat the remaining extreme-temperature heat-rejection capacity as a temporally shiftable resource rather than solving every design-hour deficit with evaporation or permanent dry-cooler overbuild.

That gives a technically credible path to near-zero operational freshwater cooling consumption in a hot climate while making the cost visible: more air-moving hardware and land, a roughly 100–200 MWh-class thermal store for a 100 MW campus depending on weather, additional controls and liquid-system maintenance, plus several megawatts of electrical cooling demand when the atmosphere becomes too hot to serve as the required heat sink.