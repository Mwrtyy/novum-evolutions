I used the attached NOVUM methodology as the governing framework for the architecture below.

1. Problem reframing

Challenge: achieve near-zero operational freshwater consumption for a high-density AI data center in a hot climate, while keeping the consequences for electricity, land, equipment, maintenance, and availability explicit.

The strongest practical baseline has recently moved. Full-liquid AI hardware can now tolerate much warmer coolant: ASHRAE defines W45 as facility liquid up to 45°C and W+ above 45°C, while NVIDIA's Rubin design uses roughly 45°C inlet and 55°C outlet coolant. That makes closed-loop dry cooling possible without cooling towers in many locations. Microsoft and Meta are likewise deploying closed-loop liquid systems that avoid evaporative cooling.

The remaining hot-climate problem is the last temperature difference to ambient. When outdoor air approaches the required facility-water temperature, a dry cooler either needs much more heat-exchanger area and airflow, mechanical refrigeration, or some way to move heat rejection to a cooler time. Evaporative cooling solves that thermodynamically very well, but by consuming water. DOE explicitly notes the water-versus-electricity trade-off: dry cooling saves on-site water but can increase electrical consumption and potentially shift water demand upstream to electricity generation.

So the useful reframing is:

Reject essentially all AI-compute heat in a hot climate with ≤0.05 L of operational freshwater per kWh of IT energy, while avoiding full-load mechanical chilling and without making extreme dry-cooler oversizing the only solution.

2. Frontier and opportunity gap

The frontier looks like this:

Region	Current state
Saturated	Cooling towers; hybrid wet/dry coolers; ordinary chilled-water storage; direct-to-chip liquid cooling; oversized dry coolers
Emerging	W45/W+ full-liquid AI racks, including components that formerly required server fans; higher return-water temperatures; sophisticated flow/setpoint control
Blocked	Pure dry rejection during the hottest hours, because ambient temperature collapses the useful approach temperature
Neglected opportunity	Store only the heat that the dry coolers cannot reject during those hours, at warm rather than refrigerated temperatures
Core contradiction	Water-efficient rejection wants large temperature differences and large air-side hardware; compact/low-power rejection wants evaporation

NVIDIA now describes a conventional cooling-tower reference of roughly 2.6 million gallons per MW-year versus near-zero cooling-water consumption for suitable W45 dry-cooler designs. That figure is not universal, but it corresponds to roughly 1.1 L/kWh and illustrates the scale of the potential site-water reduction.

3. Mechanism-diverse portfolio

A compact portfolio produces the following result:

Architecture	Central mechanism	Main reason not selected
Oversized W45 dry coolers	Buy enough coil/fan capacity for extreme ambient	Technically sound, but land, metal, fan power and peak-design capex are high
Dry coolers + air-cooled chillers	Refrigerate only when ambient is too hot	Strong baseline, but hottest hours coincide with poor chiller efficiency and grid stress
Dry + evaporative trim	Wet the incoming air during extremes	Excellent thermodynamics, but preserves exactly the freshwater dependency being reduced
Full-load thermal storage	Move several hours of the entire cooling load to night	Storage becomes unnecessarily enormous at 50–500+ MW scales
Ground/borehole sink	Put peak heat into soil/rock	Thermal saturation, drilling cost and geology make it strongly site-dependent
Seawater/brackish rejection	Transfer heat to a non-freshwater sink	Attractive near coasts, but corrosion, biofouling, pumping and thermal-discharge permitting dominate
Workload thermal shifting	Run deferrable training when rejection is easier	Useful secondary lever, but cannot cool latency-sensitive and continuous workloads
Deficit-buffered warm dry cooling	Store only the temporary difference between IT heat production and available dry-rejection capacity	Best constraint fit; chosen architecture

Thermal storage itself is emphatically not new. Amazon has prior art around PCM-based data-center cooling, Baidu has patented thermal-buffer arrangements, and 2026 research explicitly combines thermal storage with free cooling. Multiple cooling-temperature loops also have substantial prior art.

The useful innovation delta is therefore narrower:

Instead of storing “cooling” for the data center, maintain W45/W+ compute at warm temperature and store only the instantaneous dry-rejection deficit, after extracting as much heat as ambient air can accept.

That difference matters because storage capacity then scales with the peak rejection shortfall × duration, rather than IT power × duration.

4. Proposed architecture: deficit-buffered W45 dry cooling

The architecture has four thermal layers.

Layer A — fully liquid AI racks. Use W45/W+ compatible direct-to-chip/full-liquid servers. A representative operating point is approximately 45°C rack inlet and 55°C return, rather than feeding 15–25°C chilled water to the racks. NVIDIA has demonstrated the former regime, while ASHRAE's newer classes explicitly extend through W45 and beyond.

Layer B — thermal-grade separation. Do not force every facility heat load onto the coldest loop. The accelerator/CPU/networking liquid loop carries the dominant high-temperature heat stream. Electrical rooms, UPS losses, occupied spaces and any legacy equipment that genuinely need lower temperatures use a physically separate, much smaller cooling system. Multiple-temperature cooling is itself known; its role here is to prevent perhaps 5–10% of low-grade heat from dictating the temperature of the other 90–95%.

Layer C — dry rejection first. Hot facility fluid reaches an N+1 bank of large air-to-liquid dry coolers. They reject as much heat as ambient conditions permit. They are not sized around the fiction that a rare 47–50°C afternoon must be handled with the same approach temperature and efficiency as an ordinary day.

Layer D — warm thermal-headroom store. Downstream of the dry coolers, a stratified thermal store trims the facility liquid back to the temperature needed by the CDUs. The store is charged at night, when the same dry-cooler plant has more temperature headroom, and discharged only when daytime ambient conditions produce a rejection deficit.

The storage loop should be separated from the chip coolant by plate heat exchangers. That permits inexpensive treated reclaimed water, a water/glycol mixture, or a rock-filled thermocline system to be used as the bulk storage medium without exposing cold plates or server manifolds to questionable water chemistry.

A conservative implementation would use a large sensible-heat thermocline rather than novel PCM chemistry. Packed-rock thermal stores are well-established at larger temperature ranges and can achieve high thermal efficiency, although particle sizing creates a pressure-drop versus heat-transfer trade-off. PCMs make the tank smaller but introduce material ageing, compatibility and replacement risks that are unattractive in a hyperscale reliability envelope.

A modular air-cooled heat-pump/chiller bank remains in the design. The important distinction is that it is sized for the maximum credible rejection deficit, not necessarily for the complete 100-MW compute load. It activates when the thermal store is exhausted or when nights remain too warm to recharge it.

5. Illustrative 100-MW reference design

Consider a 100-MW IT campus. These are sizing assumptions, not claimed measured performance.

Suppose roughly 95 MW of heat is captured in the warm liquid loop. On a severe afternoon, assume the dry-cooler field can temporarily reject all but 30 MW of that load. If the difficult period lasts four to six hours, the thermal store needs approximately 120–180 MWhₜₕ, not 380–570 MWhₜₕ for the complete liquid-cooled load.

With a usable 15 K sensible-temperature swing, that corresponds approximately to:

Parameter	4-hour peak	6-hour peak
Unrejected heat	30 MWₜₕ	30 MWₜₕ
Stored thermal energy	120 MWhₜₕ	180 MWhₜₕ
Water-equivalent sensible volume	~6,900 m³	~10,300 m³
Illustrative packed-rock volume	~14,400 m³	~21,600 m³
Storage-branch liquid flow at 10 K ΔT	~0.72 m³/s	~0.72 m³/s

Those are not small numbers. The pipes, valves and heat exchangers are industrial-scale, and several thousand cubic metres of storage is a real civil structure.

But the comparison is important: storing the entire 95-MW heat load for six hours would require more than three times the storage. The architecture obtains most of its advantage by not putting heat into storage when the dry coolers can already reject it.

An underground or partially buried store beneath the dry-cooler yard could reduce additional land take, but that exchanges visible land use for excavation cost, waterproofing, leak detection and harder maintenance access.

6. Water, energy, land and maintenance are not all wins

Freshwater. Normal heat rejection contains no cooling tower, wetted media or misting stage. The server and facility loops are sealed. Initial fills and subsequent maintenance makeup still exist; using treated reclaimed water on the storage/facility side would keep those from becoming significant potable-water demands. “Zero water” should therefore mean no routine evaporative process-water consumption, not literally that the campus never uses water.

Electricity. There is no free thermodynamic win. The design adds storage-loop pumping and may deliberately run dry-cooler fans harder at night to recharge the reservoir. During prolonged extreme weather, its air-cooled chillers consume substantial electricity exactly when air-cooled refrigeration operates least efficiently. Whether annual electricity is lower than a very large dry-cooler plant depends on climate and equipment curves. DOE's warning about upstream water therefore applies: a site can achieve excellent WUE while using extra grid electricity generated by water-consuming thermal plants.

Land and materials. Dry coolers require considerably more air-side heat-exchanger area than evaporative towers, and ASHRAE specifically notes the larger footprint associated with large dry-cooler installations. Thermal storage adds tanks or underground structures, steel/concrete, insulation, piping and containment. The storage may let the extreme-weather dry-cooler field shrink, but it does not make the heat-rejection infrastructure disappear.

Maintenance. Cooling-tower blowdown, drift, scale control and biological-management obligations disappear, which is valuable. In their place come extensive finned-coil cleaning—especially important in dusty desert climates—fan and motor maintenance, storage-tank chemistry, large valves, heat exchangers, redundant pumps, strainers, glycol monitoring where used, and thermal-stratification instrumentation.

Server maintenance. Full-liquid cooling creates more fluid connections within the IT environment. Standardization work around CDUs, cold plates, chemistry, commissioning and maintainability is active precisely because these interfaces create operational requirements that air-cooled fleets did not have.

7. Reliability architecture

The thermal store cannot be treated like dependable infinite cooling capacity. It is a finite state-of-charge device.

The plant should therefore use two independently isolatable storage trains, redundant CDU and facility pumps, N+1 dry-cooler cells, redundant plate heat exchangers, and modular N+1 air-cooled refrigeration for the specified peak deficit. A straight bypass around the storage plant must allow the dry-cooler/chiller system to run if the storage subsystem is unavailable.

Control also needs a hard separation between optimization and protection. Weather forecasting can decide when to pre-cool the store and how aggressively to use it, but rack-inlet-temperature protection, pump sequencing and emergency chiller starts should remain deterministic local controls. Losing a forecast service or supervisory controller must not become a cooling outage.

The hardest reliability case is not the record afternoon. It is a multi-day heat event with warm nights. If nighttime ambient conditions cannot restore thermal headroom, the store progressively ceases to help and the plant becomes an ordinary dry-cooler-plus-air-cooled-chiller system. That fallback needs to be designed openly rather than hidden behind annual-average performance.

8. Boundary conditions

This architecture is strongest in a hot climate with a useful diurnal temperature swing: extremely hot afternoons but nights sufficiently cooler than the W45 facility loop.

It becomes progressively less compelling when night temperatures remain close to 40–45°C for long periods, when most installed AI hardware still requires W27/W32 water, when the site cannot accommodate substantial air-side heat exchangers, or when local electricity is so capacity-constrained that even occasional air-cooled refrigeration is unacceptable.

A coastal facility with a legally and environmentally acceptable seawater sink may rationally choose seawater heat rejection instead. Conversely, a site with abundant non-stressed reclaimed water and extremely constrained electricity could rationally retain some evaporative cooling. Reducing freshwater is a design objective, not a justification for ignoring the other resource constraints.

9. Honest verdict

Classification: differentiated architecture, with component-level novelty unverified.

The supporting physics are strong. W45/W+ liquid cooling is real; closed-loop dry rejection is real; thermal storage is real; multiple cooling-temperature loops are real.

The proposal's defensible contribution is their specific integration around peak dry-rejection deficit: capture AI heat at the highest validated temperature, keep lower-temperature loads segregated, reject everything possible directly to air, buffer only what the air cannot take during the hottest hours, and retain mechanical lift for depletion and extreme-event reliability.

The largest unresolved prior-art region is broad patent coverage around liquid-cooled data centers combined with thermal buffers and dry coolers; one recent patent application already describes a thermal-storage tank interacting with a dry cooler. I would therefore not describe this architecture as patent-novel without a much deeper claims-level search.

Its weakest physical assumption is nighttime recharge availability. If a site's hourly climate data show insufficient nocturnal temperature headroom for a significant fraction of summer, the storage layer becomes expensive infrastructure that merely postpones air-cooled refrigeration. In that regime, the technically cleaner answer is W45/W+ liquid cooling plus appropriately sized dry coolers and high-efficiency air-cooled mechanical trim, accepting the electricity and land penalty rather than disguising it as a water-saving breakthrough.