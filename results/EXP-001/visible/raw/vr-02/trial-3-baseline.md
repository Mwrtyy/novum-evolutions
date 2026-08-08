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