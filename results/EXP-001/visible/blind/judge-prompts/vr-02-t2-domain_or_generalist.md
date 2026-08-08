# EXP-001 Blind Judge — vr-02-t2-domain_or_generalist

You are evaluating two anonymized answers to the same task. You must not infer or speculate about which system produced A or B. Judge only the text shown.

Evaluator role: `domain_or_generalist`
Independence level for this run: `separate_context_same_model`

Act as a domain-or-generalist judge. Evaluate technical plausibility, mechanism quality, usefulness, constraint fit, evidence calibration, and whether the answer would actually help a competent practitioner.

Score BOTH A and B from 0 to 10 on every dimension:
- mechanism_novelty
- mechanistic_depth
- constraint_fit
- usefulness
- evidence_calibration
- falsifiability
- prior_art_awareness
- simpler_substitute_discipline
- clarity

Choose preference `A`, `B`, or `tie`. Use critical_flags for concrete serious issues. Keep rationale evidence-based and concise.

Return ONLY one valid JSON object with this exact structure and every score populated:

```json
{
  "pair_id": "vr-02-t2",
  "evaluator_id": "vr-02-t2-domain_or_generalist",
  "evaluator_role": "domain_or_generalist",
  "independence": "separate_context_same_model",
  "scores": {
    "A": {
      "mechanism_novelty": 0.0,
      "mechanistic_depth": 0.0,
      "constraint_fit": 0.0,
      "usefulness": 0.0,
      "evidence_calibration": 0.0,
      "falsifiability": 0.0,
      "prior_art_awareness": 0.0,
      "simpler_substitute_discipline": 0.0,
      "clarity": 0.0
    },
    "B": {
      "mechanism_novelty": 0.0,
      "mechanistic_depth": 0.0,
      "constraint_fit": 0.0,
      "usefulness": 0.0,
      "evidence_calibration": 0.0,
      "falsifiability": 0.0,
      "prior_art_awareness": 0.0,
      "simpler_substitute_discipline": 0.0,
      "clarity": 0.0
    }
  },
  "preference": "A",
  "critical_flags": [],
  "rationale": ""
}
```

---

# Blind pair vr-02-t2

## Task

Propose a technically plausible architecture that reduces freshwater consumption for AI compute cooling in a hot climate without hiding the energy, land, maintenance, or reliability trade-offs.

## Output A

Using the attached NOVUM methodology as the governing approach, the strongest candidate is a warm-liquid, residual-heat-buffered dry-cooling architecture: remove essentially all server heat with high-temperature direct liquid cooling, reject whatever heat ambient air can accept immediately, temporarily store only the unrejected remainder during the hottest hours, and discharge that heat to air after ambient temperature falls. This targets freshwater consumption without pretending heat rejection, electricity, land, or maintenance disappear.

1. Problem reframing

Assume a new 100 MW IT-load AI facility in a hot, water-stressed climate, with summer daytime temperatures approaching roughly 45–50°C but materially cooler nights.

The challenge becomes:

Reduce on-site freshwater consumed for cooling by >95%, while maintaining high-density AI compute availability, without replacing water consumption with an undisclosed increase in electricity, land, refrigerant infrastructure, maintenance burden, or thermal risk.

The strongest practical baseline is already quite good: warm direct-to-chip liquid cooling feeding dry coolers, with an air-cooled mechanical chiller for conditions where ambient air is too hot. NVIDIA's current Vera Rubin designs support liquid inlet temperatures up to 45°C and describe dry-cooler operation as a route to near-zero facility cooling-water consumption in suitable climates; Microsoft is likewise deploying closed-loop designs that eliminate evaporative cooling water.

The remaining hard case is therefore not moving heat out of the chips. It is rejecting approximately 100 MW of continuous low-grade heat when outdoor air is almost as hot as the allowable facility coolant.

2. Frontier and opportunity gap

The main families are already well explored:

Approach	Water	Main hidden price
Evaporative tower	High	Water withdrawal/consumption, treatment, blowdown
Warm liquid + dry cooler	Near-zero operational water	Large air-side plant; performance falls at extreme ambient
Dry cooler + air-cooled chiller	Near-zero	Compressor electricity and additional peak grid capacity
Reclaimed-water evaporation	Low freshwater	Still consumes water; treatment, salts and competing reuse demand
Immersion + dry cooling	Near-zero	Fluid compatibility and difficult maintenance workflow
Ground/aquifer rejection	Low	Land/geology, drilling and long-term thermal saturation
Radiative cooling	Low	Very low W/m² and therefore enormous area
PCM thermal storage	Low	Material mass, heat-exchanger area, cycling and controls

DOE/LBNL explicitly cautions that low site WUE can trade against higher PUE: waterless air-cooled systems commonly consume more electricity than evaporation-based cooling.

Thermal storage for data-center cooling is also existing prior art, including PCM systems and nocturnal regeneration. Recent work reports overnight-regenerating PCM concepts, while patents already disclose data-center thermal-storage architectures.

The opportunity gap is narrower:

Don't thermally store the entire data-center load. Store only the fraction that the dry coolers cannot reject during the handful of hours when ambient conditions violate the required coolant approach temperature.

3. Proposed architecture: residual-heat-buffered dry cooling
Thermal path

AI rack → 45°C liquid loop → CDU → facility loop → high-side dry cooler → warm PCM buffer → facility supply

A plausible operating envelope is approximately:

rack coolant: 45°C supply / up to ~55°C return;
facility water upstream of the CDU: roughly 40–41°C supply, depending on heat-exchanger approach;
completely sealed IT and facility coolant circuits.

NVIDIA hardware already documents 45°C maximum liquid inlet and, for some current liquid-cooled hardware, 55°C maximum return.

Stage A — reject high-grade heat first

Hot facility return water first passes through conventional modular dry coolers.

When ambient is low enough, this stage handles the entire load and the storage bank is bypassed. During a 45–48°C afternoon it may no longer be able to produce the required ~40°C facility supply—but it can still remove some energy from the hottest return stream.

That detail matters: the storage bank sees only the thermal residual after the atmosphere has taken everything it can economically take.

Stage B — warm thermal buffer

Downstream sits a bank of independently isolatable PCM heat exchangers, using an encapsulated material with a transition temperature roughly around 37–40°C.

During the hottest period:

return heat passes through the dry cooler;
remaining heat melts PCM;
the PCM bank clamps the facility supply close to the temperature required by the CDUs.

This is warm thermal storage, not an ice battery. There is no deliberate production of chilled water.

At night, valves reverse the role of the dry-cooler plant: cooler outdoor air solidifies the PCM while simultaneously serving the live IT load.

Salt hydrates are credible candidate materials in this temperature range, but they bring nontrivial concerns including supercooling, phase separation, leakage, conductivity and cycle stability. Those problems have to be engineered rather than assumed away.

Stage C — mechanical safety net

A modular air-cooled trim-chiller plant remains installed.

It operates when:

nights remain too warm to regenerate storage;
a heat wave lasts longer than the storage design duration;
dry-cooler capacity is impaired;
part of the PCM bank is offline.

For a facility promising strict availability, I would retain enough mechanical capacity to meet the design-basis heat rejection requirement without depending on workload throttling.

That is expensive and intentionally so: thermal storage reduces runtime and peak coincidence, not necessarily the amount of emergency equipment a high-availability facility must own.

4. What is actually different

Remove the ordinary components—liquid cooling, dry coolers, PCM and chillers—and the irreducible architectural change is:

The thermal store is placed after first-stage sensible air rejection and sized dynamically for the ambient-exceedance residual rather than for the full IT cooling load.

Conventional thermal-storage designs commonly store "cold" or buffer the total cooling service. Here the control variable is unrejected heat, QIT − Qdry(Tambient).

Conceptually:

QPCM(t)=max[0,QIT(t)−Qdry(t)]

The storage therefore grows according to the integral of that residual over a heat event, rather than IT MW × the entire hot-period duration.

I would classify the result as a differentiated architecture, not claim a new fundamental cooling mechanism. The search finds substantial neighboring PCM, night-cooling and dry-cooling prior art, so stronger novelty claims would be unjustified.

5. Order-of-magnitude design for 100 MW IT

Suppose a severe afternoon lasts six hours and the dry coolers still reject 60% of the heat. The PCM bank must absorb:

100 MW × 40% × 6 h ≈ 240 MWhₜₕ.

At an effective installed storage density around 40 kWhₜₕ per tonne after allowing for incomplete utilization and system losses, that is approximately 6,000 tonnes of PCM.

An eight-hour or worse event can readily push the bank toward 8,000–12,000 tonnes.

This is not a compact battery hiding behind the building. It is industrial infrastructure, potentially several thousand cubic metres of storage plus heat exchangers, piping and access space.

The dry-cooler plant is substantial too. Contemporary 2 MW dry-cooler packages can occupy about 31 m² of bare equipment footprint and draw tens of kilowatts of fan power at rated conditions; actual W45 performance at extreme ambient temperatures requires derating, redundancy, clearances and potentially additional capacity for nighttime PCM regeneration.

A reasonable planning allowance for a 100 MW installation is therefore on the order of 0.5–2+ hectares for the heat-rejection field, plus perhaps another fraction of a hectare for thermal storage, before accounting for acoustic setbacks and the backup chiller plant.

6. Resource ledger

Freshwater. Normal cooling operation has no evaporative heat rejection, so freshwater consumption can approach zero apart from initial filling, maintenance, leakage and coolant replacement. For scale, Microsoft's FY2024 global WUE reference of 0.30 L/kWh corresponds to roughly 263 million litres/year at a constant 100 MW IT load; NVIDIA cites conventional cooling-tower consumption corresponding to roughly 984 million litres/year at the same scale. Those figures are different baselines, not directly interchangeable measurements.

Energy. Water savings are not free. One 2026 UC Davis study modeled a chiller-less liquid/dry-cooler system at 40°C outdoor temperature with cooling electricity around 2.1% of compute power under its studied conditions. Extreme heat, lower coolant temperatures, storage pumping and mechanical backup increase that number. I would not promise an annual PUE improvement over a well-designed evaporative plant without site-specific simulation.

Land and materials. Expect thousands of tonnes of PCM, extensive aluminum/copper coil area, large pipe headers, potentially hundreds of fans and a sizable mechanical yard. Dry cooling saves water partly by buying heat-transfer surface.

Maintenance. The main burdens become dusty/fouled dry-cooler coils, EC fans and bearings, pumps, CDU filters, coolant chemistry, valves, PCM encapsulation integrity and storage performance degradation. Salt-hydrate formulations particularly need monitoring for segregation and supercooling. Full mechanical backup also preserves the usual compressor and refrigerant maintenance.

Reliability. A PCM module failure should reduce thermal endurance rather than interrupt cooling; banks should therefore be segmented with independent isolation and bypass. Pumps, CDUs and fan groups require N+1 design. Sandstorms or coil fouling become waterless cooling's equivalent of cooling-tower water-quality risk.

Local environmental impact. Nearly the entire electrical load ultimately still becomes heat dumped into the surrounding air. The architecture does not eliminate thermal plumes or fan noise; nighttime regeneration may move a larger share of both into evening/night hours.

Source water. "Zero site cooling water" is not equivalent to zero water footprint if the additional electricity comes from generation technologies that themselves consume water. LBNL specifically distinguishes site and source WUE for this reason.

7. The weakest assumption

The architecture depends most strongly on diurnal temperature recovery.

If a site's severe heat waves routinely produce nights too warm for the dry coolers to bring the PCM below its solidification temperature, the storage cannot reset. After one or two days it becomes dead thermal mass and the facility falls back to its air-cooled chillers.

That gives a clean kill condition:

If design-year weather and actual dry-cooler performance show that the PCM cannot reliably regenerate between successive hot periods—or if doing so requires so much oversized fan/coil capacity that the storage no longer reduces mechanical cooling—the thermal buffer should be deleted and the facility should use straightforward warm-liquid dry cooling plus air-cooled chillers.

The same analysis may show that some hot climates are excellent fits because of large day/night swings, while hot-humid climates with warm nights are poor fits.

Verdict

The proposed system is technically plausible with currently available classes of hardware:

45°C-class direct liquid cooling + isolated facility loop + staged dry heat rejection + modular ~38–40°C latent-heat storage + nighttime regeneration + full air-cooled emergency trim.

Its strongest advantage is not "waterless cooling" by itself—that is already achievable. Its useful mechanism is time-shifting the specific fraction of heat that dry cooling cannot reject during extreme afternoon conditions, potentially avoiding substantial hot-hour compressor operation while retaining near-zero on-site freshwater consumption.

The price is visible: thousands of tonnes of thermal-storage material, more heat-exchanger area, roughly hectare-scale additional plant, more valves and controls, PCM lifecycle uncertainty, and mechanical backup that cannot be eliminated when high availability matters. In climates without sufficiently cool nights, the simpler dry-cooler/chiller baseline is the better architecture.

## Output B

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

