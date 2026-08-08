Using the attached NOVUM methodology as the governing frame, the strongest defensible answer is a differentiated architecture rather than a claim of novel cooling physics.

1. Problem reframing

The engineering problem is:

Reduce on-site freshwater consumed for cooling by at least ~90% relative to an evaporative/adiabatic design for a high-density AI facility in a hot climate, while preserving the same compute-availability requirement and making any increase in electricity, heat-rejection area, equipment count, maintenance burden, or compute curtailment explicit.

The strongest practical baseline is already fairly good: high-temperature direct-to-chip liquid cooling feeding closed-loop dry coolers, with mechanical refrigeration or adiabatic assist when ambient temperature gets too high. ASHRAE's current AI-data-center framework describes facility-water supply temperatures as high as 45°C, returns around 65°C, and direct dry heat rejection in warm climates. The problem occurs when outdoor air approaches the required coolant-supply temperature: the dry cooler loses the temperature difference that makes passive heat rejection work.

This is not hypothetical. Microsoft is deploying closed-loop, zero-evaporation liquid cooling, while explicitly acknowledging that replacing evaporative heat rejection with mechanical cooling produces some energy penalty. A recent waterless Australian project likewise illustrates the water-versus-electricity trade-off rather than making it disappear.

2. Frontier and opportunity gap

The obvious answers are already occupied. Direct-to-chip cooling plus dry coolers is established; NLR/DOE has demonstrated hybrid dry/wet heat rejection; warm-water cooling combined with night-charged stratified thermal storage was studied as far back as 2016; thermal-aware compute scheduling is also established; and even radiative data-center heat rejection has patent prior art.

The useful opportunity is therefore narrower: do not design the entire cooling plant around the few hours when maximum AI load coincides with maximum outdoor temperature. Instead, create an explicit thermal-capacity layer between the GPUs and the outside air, then expose that capacity to the compute scheduler.

The underlying contradiction cannot be engineered away:

Zero evaporation + very hot ambient + continuous maximum compute = either more heat-exchanger area, more electrical work, temporal storage, exported heat, or reduced/shifted compute.

Any proposal claiming otherwise is probably hiding one of those resources.

3. Four mechanism-distinct candidates
Candidate	Irreducible mechanism	Main cost transferred to	Verdict
A. Worst-case dry plant	Warm-water direct-to-chip cooling with enough dry cooler/chiller capacity for design-peak ambient	Land, aluminum/copper, fans, electrical peak capacity	Survives as baseline. Technically conservative but expensive to size for rare extremes.
B. Diurnal heat buffer	Store the portion of heat that cannot be rejected during the hottest hours; reject it later when ambient falls	Tank volume, night fan/pump energy, controls	Survives. Mechanism is known, but well matched to climates with useful day/night temperature swing.
C. External heat sink	Raise/export 55–65°C return heat to an industrial or district-heat consumer rather than rejecting it locally	Pipelines, heat pumps, dependence on an off-taker	Conditional. Excellent where a reliable year-round sink exists; poor as a generic architecture.
D. Compute-shaped heat generation	Treat flexible AI training as a controllable thermal load and reduce/shift it when heat-rejection headroom collapses	GPU utilization, completion time, orchestration complexity	Survives as an adjunct, not as the sole reliability mechanism. Thermal-aware scheduling is already known.

Candidate B is the best physical core. Candidate D makes B substantially smaller. Candidate C should be added opportunistically where the site has a credible heat customer, but the cooling plant must remain safe if that customer disappears.

4. Proposed architecture: thermal-headroom–buffered dry cooling

The resulting architecture is:

GPU/CPU cold plates
        ↓
redundant rack CDUs
        ↓
43–60°C closed facility-water loop
        ↓
     thermal bus
   ↙      ↓       ↘
dry       stratified     high-temperature
coolers   water store    air-cooled trim chiller
   ↘      ↓       ↙
      43–45°C supply
           ↓
          CDUs

Thermal controller ⇄ cluster scheduler
     ↑
ambient forecast + storage state + dry-cooler capacity

The rack side uses conventional single-phase direct-to-chip cold plates and CDUs, not an exotic working fluid. The facility loop operates as hot as the selected hardware warranty allows—approximately in the W40/W45 regime—because every degree of higher coolant temperature increases the number of hours in which ambient air can reject heat without refrigeration. ASHRAE explicitly identifies high-temperature liquid loops as the enabler for water-free dry cooling.

Dry coolers are then not sized to magically handle full IT power at the site's absolute record temperature. They are sized around a chosen high-percentile operating condition plus redundancy. During ordinary conditions they reject the full load and recharge the thermal store.

During a very hot afternoon, suppose a 100 MW IT facility can reject only 75 MW through its dry plant while keeping supply water inside the hardware limit. The remaining 25 MW thermal deficit goes into a closed stratified water tank. For four hours, that represents 100 MWh of stored heat.

With an approximately 18 K usable temperature swing, simple sensible-water storage requires roughly:

100 MWh × 3,600 MJ/MWh ÷ (4.18 MJ/m³-K × 18 K) ≈ 4,800 m³ of water.

That is roughly a 25 m diameter tank with about 10 m of usable water depth. It is substantial civil infrastructure, but not physically extraordinary for a hyperscale campus. A severe 50 MW deficit lasting eight hours would need roughly 19,000 m³, illustrating why storage cannot be waved away as a free solution.

At night the dry plant rejects both the continuing IT heat and the stored heat. The facility therefore trades daytime water consumption for additional nighttime fan/pump operation and installed heat-exchanger capacity.

5. The key control mechanism

The useful architectural delta is the interface between facilities and compute.

Rather than giving the cluster scheduler only an electrical power cap, the facility controller continuously publishes a thermal-headroom envelope, for example: “28 MW of additional heat is sustainable for 40 minutes; 14 MW for the following three hours; reserve storage must remain above 20%.”

Latency-critical inference and high-priority training retain guaranteed thermal capacity. Checkpointable or delay-tolerant training consumes the remaining envelope. As storage approaches its reliability reserve, flexible jobs are slowed, checkpointed, migrated, or deferred before hardware temperatures become the control signal.

This is deliberately not a black-box AI controller. The hard constraints—maximum facility-water temperature, CDU flow, minimum thermal-storage reserve, pump redundancy and trim-chiller capacity—remain deterministic safety interlocks. Contemporary work already points toward exchanging workload heat envelopes, cooling capacity, and storage state between IT and facility controls, so the mechanism should be regarded as a practical architectural integration rather than a unique invention.

6. Where the costs actually go
Resource	Consequence of the architecture
Freshwater	Routine evaporative cooling can be eliminated. Water remains in closed loops and the thermal tank; there is initial fill, chemistry-management makeup and leakage/service replacement. “Zero evaporated cooling water” is not literally zero water used by the entire site.
Electricity	Usually more than an evaporative tower during the difficult hot hours. Dry-cooler fans run harder, stored heat must later be rejected, and the trim chiller consumes compressor power during prolonged extremes. Annual magnitude depends strongly on hourly climate.
Indirect water	Not eliminated. Extra electricity can have a water footprint at the generating plant; LBNL finds data-center workload water footprints vary enormously with grid, cooling architecture, server efficiency and location.
Land/material	More outdoor coil surface plus one or more thermal tanks. As an illustrative equipment point, a commercial ~1.2 MW dry cooler rated at 35°C ambient occupies about 7 × 2.6 m before spacing and service clearances; a 100 MW plant needs many dozens, with additional derating and redundancy in a hotter design condition.
Maintenance	Adds CDU filters/pumps, coolant chemistry, leak detection, fan arrays, fin cleaning in dusty climates, tank diffusers/thermocline monitoring, large isolation valves and an air-cooled refrigeration subsystem.
Reliability	Storage provides time, not infinite cooling capacity. A multi-day heatwave can exhaust the benefit. The air-cooled trim system therefore cannot be eliminated unless the operator accepts compute curtailment.
Compute utilization	Flexible training may run more slowly during the worst thermal periods. If GPU-hours are more valuable than the avoided cooling infrastructure, the controller should instead run the trim chiller.

There is also an important accounting trap: a spectacularly low site WUE does not prove low total water impact. LBNL's analysis finds that electricity-related water, server efficiency and utilization can materially change workload-level water consumption, sometimes by orders of magnitude.

7. Reliability architecture

For mission-critical operation, I would use N+1 or better CDUs and facility pumps, redundant dry-cooler cells with isolation valves, independent powered coolant circulation through electrical transfer events, and a thermal-store reserve that operations is forbidden to consume for ordinary economic optimization.

The trim chiller is the last physical line of defence during long hot spells. If it reaches capacity, the sequence is controlled reduction of deferrable training, then broader GPU power caps, and only finally hardware thermal throttling. The design therefore never relies on an invisible emergency switch to freshwater evaporation.

This matters because ASHRAE itself notes that pure dry cooling can otherwise end in thermal throttling when ambient conditions exceed the dry-cooler limit.

8. Boundary conditions

This architecture is strongest in a hot-arid climate with meaningful nighttime cooling, where heat can genuinely be shifted from a 45–48°C afternoon into a substantially cooler night.

It becomes less attractive in hot-humid locations where nights remain very warm, because the tank cannot recharge cheaply. There the trim chiller gets larger, annual electricity rises, and brute-force waterless mechanical cooling may be simpler.

It also becomes unattractive if the accelerator platform requires low facility-water temperatures. Conversely, future W+ hardware capable of facility supply temperatures above 45°C makes the concept substantially easier because dry heat rejection gains more temperature headroom.

9. Rejected directions

The red-team removed several seductive options. PCM storage was dropped because data-center PCM cooling already has significant prior art and brings material compatibility, fire/cycling and replacement questions without being necessary here. Radiative roof cooling was rejected as a primary sink because its heat flux would require enormous surface area at AI-campus scale and radiative data-center systems already have patent activity.

Aquifer or reservoir thermal storage can outperform tanks in favorable geology and is actively being studied for data centers, but it introduces hydrogeology, drilling, permitting, groundwater chemistry and long-term thermal-plume dependencies that prevent it from being the generic answer.

10. Falsifiable verdict

Verdict: differentiated architecture; technically plausible; novelty of the individual mechanisms does not survive the prior-art scan.

The central claim worth retaining is narrower: a hot-climate AI campus can eliminate routine freshwater evaporation without sizing its entire dry/refrigeration plant for the worst coincident ambient-and-compute condition, by explicitly buffering the temporary heat-rejection deficit and making thermal headroom a schedulable compute resource.

The architecture should be rejected for a particular site if hourly weather and workload traces show that storage routinely fails to recharge overnight, if the required store grows into several hundred MWh merely to survive normal summer conditions, if flexible workload is too small to matter, or if the resulting annual compressor/fan electricity makes a conventional worst-case dry plant simpler and cheaper. Those are the conditions under which the water savings are being purchased with too much energy, land or operational fragility rather than genuinely improving the system.