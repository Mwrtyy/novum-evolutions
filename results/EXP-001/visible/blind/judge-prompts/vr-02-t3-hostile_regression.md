# EXP-001 Blind Judge — vr-02-t3-hostile_regression

You are evaluating two anonymized answers to the same task. You must not infer or speculate about which system produced A or B. Judge only the text shown.

Evaluator role: `hostile_regression`
Independence level for this run: `separate_context_same_model`

Act as a hostile regression judge. Search aggressively for hidden regressions, fake novelty, unsupported claims, broken constraints, weak causal mechanisms, and failures of falsification. Do not reward verbosity.

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
  "pair_id": "vr-02-t3",
  "evaluator_id": "vr-02-t3-hostile_regression",
  "evaluator_role": "hostile_regression",
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

# Blind pair vr-02-t3

## Task

Propose a technically plausible architecture that reduces freshwater consumption for AI compute cooling in a hot climate without hiding the energy, land, maintenance, or reliability trade-offs.

## Output A

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

## Output B

Using the attached NOVUM methodology as the governing structure, the strongest defensible architecture is a waterless temperature-grade cooling cascade: direct-to-chip warm liquid cooling, dry heat rejection first, and modular mechanical refrigeration only for the fraction of heat that ambient air cannot accept.

1. Problem reframing

Assume a reference 100 MW IT AI facility in a hot, water-stressed climate with a design outdoor dry-bulb temperature of roughly 50°C, and accelerators capable of warm-liquid cooling near the ASHRAE W45 class.

The challenge becomes:

Maintain full 100 MW compute at the design-hot condition, with essentially no routine freshwater consumed for heat rejection, while making the resulting electricity, land, equipment, maintenance, and reliability costs explicit.

The strongest conventional alternatives are evaporative cooling towers, hybrid dry/adiabatic systems, and full-capacity air-cooled chillers. Cooling towers exploit evaporation efficiently but inherently consume water; DOE explicitly identifies evaporation and blowdown as major cooling-tower water losses. Conversely, dry cooling reduces water demand but can increase electrical energy use and potentially shift water consumption upstream to electricity generation.

I would set three hard performance gates: no evaporative cooling during normal operation; no compute throttling at the specified 50°C design condition after an N+1 failure; and cooling-system freshwater makeup below roughly 0.005 L/kWh-IT, excluding the one-time initial closed-loop charge.

2. Frontier and opportunity gap

Warm-water liquid cooling is now practical rather than speculative. ASHRAE identifies W45 liquid-cooling classes, and NVIDIA's 2026 Rubin design operates with coolant up to 45°C and uses fully liquid-cooled infrastructure. Microsoft has likewise deployed designs that recirculate cooling water in a sealed loop rather than continuously evaporating it, while openly acknowledging that replacing evaporation with mechanical cooling raises PUE.

The unresolved problem appears during extreme heat. A dry cooler cannot cool a 45°C liquid stream to 45°C when the outdoor air itself is 45–50°C. ASHRAE therefore describes adiabatic assistance or thermal throttling as potential responses to extreme ambient conditions.

That gives the useful contradiction:

You can eliminate routine water consumption, but once ambient temperature approaches the required coolant temperature, physics forces you to pay with at least one of four things: electrical work, stored thermal capacity, reduced compute, or another heat sink.

Direct-to-chip cooling changes how efficiently heat reaches the plant; it does not eliminate the final heat-rejection problem.

3. Assumption graph

The critical physical chain is:

100 MW electricity → approximately 100 MW heat → liquid transport → environmental heat rejection.

The important assumptions are these:

Assumption	Classification	Consequence if false
AI hardware accepts ~45°C coolant	Hard technology constraint	Chiller energy rises sharply at lower coolant temperatures
Most rack heat enters liquid	Hard architecture constraint	Residual room cooling becomes a major colder-temperature load
Water cannot be routinely evaporated	Hard task constraint	Cooling tower/adiabatic fallback disappears
Compute must remain full-power at 50°C	Soft operational constraint	Power shaping becomes another heat-rejection resource
Heat rejection must happen instantaneously	Convention	Short-duration thermal storage can relax this
All heat needs mechanical refrigeration in extreme heat	Convention	Hot-return heat can still be rejected dry before refrigeration

The final assumption is the bottleneck worth attacking.

4. Mechanism-diverse portfolio

The frontier search produces the following portfolio rather than eight names for essentially the same cooler:

Mechanism	Main advantage	Fatal or limiting issue	Verdict
Oversized W45 dry coolers	Very simple, essentially no consumptive water	Cannot produce 45°C coolant when air exceeds it	Reject as sole system
Full air-cooled chiller	Works regardless of humidity; no cooling tower	Highest compressor load and large condenser yard	Viable baseline
Series dry rejection + trim refrigeration	Mechanically cools only the residual heat	More valves, controls, fans and chillers	Survivor
PCM/thermal battery charged overnight	Bridges hottest hours without evaporation	Storage becomes enormous at hyperscale	Constrain to short-duration reserve
Thermal-aware GPU power shaping	Converts compute flexibility into thermal capacity	Delays jobs; unacceptable for hard-SLA loads	Contingency only
Two-phase immersion	High heat-transfer capability	Fluid compatibility, serviceability and supply-chain complications	Not necessary here
Reclaimed-water evaporative tower	Very good electrical efficiency without potable water	Still consumes scarce water and requires water chemistry	Site-dependent substitute
Closed-loop borefield	Water-independent heat sink	Huge drilling/land requirement and long-term thermal saturation	Reject at 100 MW scale
Atmospheric-water/desiccant coupling	Could offset water demand	Scale and performance in hot/dry air remain insufficiently established	Reject for primary cooling

Thermal storage, workload-aware scheduling, and dry-plus-chiller cooling all have substantial prior art, including data-center PCM patents, chilled-water storage research, workload-aware cooling patents, and older free-cooling-plus-chiller architectures.

So this should not be represented as a fundamentally new refrigeration mechanism.

5. Selected architecture: Waterless Temperature-Grade Cascade

The architecture is:

AI RACKS
45°C supply → cold plates → 60–65°C return
        │
        ▼
   Rack / row CDUs
        │
        ▼
┌─────────────────────────────┐
│ STAGE 1: DRY HEAT REJECTION │
│ large ambient fin/fan banks │
└──────────────┬──────────────┘
               │
       whatever heat remains
               ▼
┌─────────────────────────────┐
│ STAGE 2: TRIM REFRIGERATION │
│ modular N+1 heat-pump plant │
│ with dry air condensers     │
└──────────────┬──────────────┘
               │
          45°C supply
               ▼
             RACKS

         ┌──────────────────┐
         │ THERMAL RESERVE  │
         │ 5–10 min closed  │
         │ loop buffer      │
         └──────────────────┘

The irreducible architectural difference is temperature-grade separation. The plant never asks a compressor to move heat that can already flow spontaneously into ambient air. The 60–65°C return stream first encounters dry coolers; only the remaining temperature drop needed to regain the rack supply setpoint crosses a refrigeration machine.

Series free cooling followed by a chiller is not itself new—older data-center prior art contains closely related arrangements. The defensible claim here is therefore a differentiated waterless architecture optimized around current W45/W+ AI equipment, rather than a novel thermodynamic cycle.

6. What happens at 50°C

A simplified 45→65°C, 100 MW loop requires about 1,200 kg/s of coolant flow if water-like heat capacity is assumed.

Suppose the dry cooler has a 5 K terminal approach. With 50°C ambient air, it can plausibly bring a 65°C return toward approximately 55°C, but not to 45°C.

That means, approximately:

Heat path at 50°C ambient	Thermal duty
Dry cooler: 65→55°C	~50 MW
Trim refrigeration: 55→45°C	~50 MW

So half the heat is still rejected without compression even though ambient air is hotter than the required supply temperature.

If the trim plant operates at an actual COP in the rough 5–7 range under these conditions, its compressors would consume approximately 7–10 MW to remove that remaining 50 MW. Pumps and enormous dry-cooler/condenser fans might add another order-of-magnitude 1–3 MW depending on coil pressure drop, approach temperature, fouling, and layout.

Thus a credible extreme-hot-hour cooling penalty is roughly 8–13 MW per 100 MW IT, rather than pretending that "zero water" means "zero cooling energy." These figures are engineering sizing estimates, not vendor performance guarantees.

At approximately 40°C ambient or below, a 45°C supply becomes much more compatible with dry-only rejection, and compressors can largely bypass. ASHRAE identifies elevated liquid temperatures precisely as an enabler for this kind of dry heat rejection.

One important catch: a CDU heat exchanger may require several kelvin of approach. If the accelerator requires 45°C on its technology-cooling side, the facility loop may actually need to provide roughly 40–42°C. That shifts the dry-only boundary downward and increases refrigeration hours. That CDU approach temperature should therefore be treated as a first-order procurement specification, not a minor mechanical detail.

7. The costs that should appear on the front page

Energy: Water savings are bought partly with electricity. During extreme heat, the trim compressors become a significant site load. Backup power must consequently support not just 100 MW of IT but potentially another ~10 MW-scale cooling load. A facility whose generators cover the servers but not peak refrigeration is not genuinely N+1. DOE specifically warns that waterless dry cooling can also move water consumption upstream if the electricity comes from water-consuming thermal power plants.

Land and airflow: Rejecting 100 MW into air is physically large. With approximately a 10 K rise in cooling air, the order of magnitude is 8,000+ m³/s of airflow for 100 MW of dry rejection. Even at peak conditions where Stage 1 carries only 50 MW, several thousand cubic metres per second remain. The plant therefore needs substantial coil area, fan arrays, acoustic treatment, maintenance aisles, and enough separation to prevent hot discharge air from recirculating into intakes. ASHRAE likewise notes the larger footprint of dry coolers compared with evaporative rejection.

Maintenance: Cooling-tower scale, blowdown treatment, drift and continuous makeup-water systems disappear, but maintenance does not. It becomes fan bearings and motors, dusty heat-exchanger fins, refrigerant compressors, leak detection, coolant chemistry, pumps, valves and cold-plate/CDU connections. Hot desert dust can degrade the exact air-side heat transfer on which the system depends, so fouling margin and cleanable coil geometry matter.

Reliability: The architecture eliminates dependence on municipal water pressure during extreme heat, but replaces it with much stronger dependence on electricity and refrigeration equipment. The trim plant should therefore be modular N+1 rather than one enormous chiller, with physically independent electrical feeds and isolation valves. A failure of the entire refrigeration bus during a 50°C afternoon otherwise removes a very large fraction of cooling capacity immediately.

8. Reliability repair: short thermal reserve, not all-day storage

I would add thermal storage only as a ride-through device, not pretend it can economically absorb an entire afternoon of 100 MW heat.

For perspective, storing 100 MW for ten minutes over a 10 K usable temperature range requires roughly 1,400 m³ of water-equivalent sensible storage. An illustrative PCM with about 180 kJ/kg latent capacity and 900 kg/m³ density would still require roughly 370 m³ before packaging, heat exchangers and redundancy.

An hour-scale or four-hour "heat battery" therefore becomes a major civil project. The sensible use is five to ten minutes: enough to bridge compressor trips, generator transfers, valve transitions or rapid GPU power reduction.

That exposes another trade-off instead of hiding it: avoiding evaporative emergency cooling costs several hundred to more than a thousand cubic metres of closed-loop thermal-buffer infrastructure.

9. Operating and failure policy

Normal operation should have three deterministic regimes. Below the dry-cooling threshold, the trim machines remain bypassed. As ambient temperature rises, dry cooling stays first in series and refrigeration progressively takes the residual. At and below the 50°C design point, the plant must maintain full IT capacity without water or workload reduction.

Only beyond design conditions or during multiple equipment failures should the compute layer become a thermal actuator. Training jobs with flexible deadlines can be briefly power-capped or checkpointed while latency-critical inference remains protected. Coordinated compute/cooling control is technically credible, but substantial prior work already exists on thermal-aware scheduling, so it should be treated as a resilience mechanism, not presented as the core invention.

For mixed-generation hardware, the architecture becomes less attractive. If only 80–85% of server heat reaches the warm liquid loop, a 100 MW campus leaves 15–20 MW of room heat requiring air handling and potentially a colder chilled-water loop. The best deployment target is therefore a new-build cluster approaching complete liquid capture; NVIDIA's Rubin reference direction demonstrates that 100% liquid-cooled equipment is now entering this design space.

10. Decision, uncertainty, and falsification gate

On a 0–10 decision scale, I would put the architecture roughly at: problem value 9; technical feasibility 8; advantage magnitude 7–9; adoption feasibility 7; testability 9; evidence confidence 8; mechanism novelty 3–5; fatal-risk severity 4–6.

The two most uncertain numbers are advantage magnitude and fatal-risk severity. Both depend heavily on the actual 50°C compressor performance map, CDU approach temperature, dust fouling, required redundancy, and the site's number of extreme-hot hours.

The decisive validation gate is simple enough to kill the architecture quickly: operate a representative ~1 MW thermal block at the intended coolant flow and a controlled 50°C air inlet. It must hold the rack-side maximum supply temperature continuously with zero evaporative assist, remain below the agreed peak parasitic-power ceiling, and survive loss of one active refrigeration module without crossing the hardware thermal limit. Failure on any of those conditions means the proposed operating envelope should be narrowed rather than rationalized away.

Verdict

Differentiated architecture; not a verified novel cooling mechanism.

What is well supported is that high-temperature liquid cooling, closed-loop water systems, dry coolers, mechanical trim cooling, thermal storage and coordinated compute controls are all technically real.

What is inferred is that arranging them as a strict dry-first temperature-grade cascade can make zero-evaporation cooling practical in a ~50°C climate without imposing the energy penalty of mechanically chilling the entire heat load during every hot hour.

The main unresolved engineering question is not whether the thermodynamics work. It is whether real compressor curves + CDU approach temperatures + hot-air recirculation + desert fouling leave enough efficiency advantage over a straightforward full air-cooled chiller plant to justify the extra plumbing and controls.

And the most important accounting rule is: report both site WUE and electricity-source water intensity. Otherwise a "zero-water" data center can simply exchange visible local water consumption for less-visible power-sector water consumption.

