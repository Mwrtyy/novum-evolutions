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