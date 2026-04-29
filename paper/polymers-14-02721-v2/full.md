Article

# Rheological Behavior and Dynamic Mechanical Properties for Interpretation of Layer Adhesion in FDM 3D Printing

Supaphorn Thumsorn  $^{1, *}$ , Wattanachai Prasong  $^{2}$ , Takashi Kurose  $^{1,3}$ , Akira Ishigami  $^{1,4}$ , Yutaka Kobayashi  $^{1}$  and Hiroshi Ito  $^{1,4, *}$

$^{1}$  Research Center for GREEN Materials and Advanced Processing, Yamagata University, 4-3-16 Jonan, Yamagata 992-8510, Japan; kurose.takashi@sist.ac.jp (T.K.); akira.ishigami@yz.yamagata-u.ac.jp (A.I.); kobayashi.y@yz.yamagata-u.ac.jp (Y.K.)  
$^{2}$  Department of Industrial Engineering, Faculty of Engineering, Pathumwan Institute of Technology, 833 Rama I Road, Wangmai, Pathumwan, Bangkok 10330, Thailand; wattanachai@pit.ac.th  
$^{3}$  Department of Mechanical Engineering, Faculty of Science and Technology, Shizuoka Institute of Science and Technology, 2200-2 Toyosawa, Shizuoka 437-8555, Japan  
4 Graduate School of Organic Materials Science, Yamagata University, 4-3-16 Jonan, Yamagata 992-8510, Japan  
* Correspondence: thumsorn@yz.yamagata-u.ac.jp (S.T.); ihiroshi@yz.yamagata-u.ac.jp (H.I.); Tel.: +81-(23)-8263081 (H.I.)

![](images/ab773abf67326f55bc4c6a1c66c122f2c82dc813fbe38df2556d1d57fa10c2d4.jpg)

# check for updates

Citation: Thumsorn, S.; Prasong, W.; Kurose, T.; Ishigami, A.; Kobayashi, Y.; Ito, H. Rheological Behavior and Dynamic Mechanical Properties for Interpretation of Layer Adhesion in FDM 3D Printing. Polymers 2022, 14, 2721. https://doi.org/10.3390/polym14132721

Academic Editor: Andrea Sorrentino

Received: 5 June 2022

Accepted: 1 July 2022

Published: 3 July 2022

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/7e563cfca97b7d00b05421b78ae818b2b82408e5190587f608251b96840d88bd.jpg)

Copyright: © 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

Abstract: Commercial filaments of poly(lactic acid) (PLA) composites with particulate filler, carbon fiber, and copper powder with different contents were fabricated by FDM 3D printing in XZ-direction at bed temperatures of  $45^{\circ}\mathrm{C}$  and  $60^{\circ}\mathrm{C}$ . The effects of additives and bed temperatures on layer adhesion, fracture behavior, and mechanical performance of the PLA composites 3D printing were evaluated. Rheological properties informed viscous nature of all filaments and interface bonding in the PLA composites, which improved printability and dimensional stability of the 3D printing. Crystallinity of the PLA composites 3D printing increased with increasing bed temperature resulting in an improvement of storage modulus, tensile, and flexural properties. On the contrary, the ductility of the 3D printing was raised when printed at low bed temperature. Dynamic mechanical properties, the degree of entanglement, the adhesion factor, the effectiveness coefficient, the reinforcing efficiency factor, and the Cole-Cole analysis were used to understand the layer adhesion, and the interfacial interaction of the composites as compared to the compression molded sheets. SEM images revealed good adhesion between the additives and the PLA matrix. However, the additives induced faster solidification and showed larger voids in the 3D printing, which indicated lower layer adhesion as compared to neat PLA. It can be noted that the combination of the additives and the optimized 3D printing conditions would be obtain superior mechanical performance even layer adhesion has been restricted.

Keywords: composite; dynamic mechanical analysis; 3D printing; layer adhesion; morphology

# 1. Introduction

Fused deposition modeling (FDM) 3D printing has been widely utilized in various industries due to its custom design and cost effectiveness [1-8]. FDM 3D printing products have formed by the layer-by-layer deposition, which exhibited anisotropic characteristic and drawbacks such as poor interlayer adhesion, incomplete printing, shrinkage and low dimension accuracy resulting in low mechanical performance and their structural failure [3,5,7-9]. The selection of filaments and the controlled printing conditions can be optimized for improving the drawbacks and obtaining superior mechanical performance of the FDM 3D printing products [1,2,10-12]. Polymer filaments are feedstocks for the FDM 3D printing. Acrylonitrile butadiene styrene (ABS), poly(lactic acid) (PLA), and poly(ethylene terephthalate glycol) (PETG) are commonly filaments for the FDM 3D printing, which have good printability at low printing temperature ranges compared to high performance

plastics, such as polycarbonate (PC), polyamide (PA, nylon), polyetherimide (PEI), and poly(ether-ether-ketone) (PEEK) [2,13-16]. The polymer filaments have been developed by the incorporation of additives, blending and estimated suitable printing conditions to diminish the FDM 3D printing drawbacks [1,5-7,9-15,17-21]. The following research performed guidelines to overcome the drawbacks. The effects of nozzles temperatures, bed temperatures, and annealing conditions on properties of the FDM 3D printing of PLA were reported by Benwood et al. [5]. The increasing in the nozzle and the bed temperatures significantly improved mechanical properties of the PLA 3D printings, which exhibited less voids and have good layer adhesion. Nguyen et al. applied carbon fiber (CF) in the lignin based ABS composite 3D printing, which the CF acted as a bridging between the printed layers and improved the interlayer adhesion in the lignin/ABS-rubber composites [10]. Ferreira et al. [20] noticed that CF highly oriented during the deposition in the 3D printing, which strongly improved tensile modulus but reduced elongation of the CF reinforced PLA composites 3D printing. Additionally, the higher printing temperature resulted in the present of bubble-like structure in the specimens and introduced the nozzle temperature lower than  $220^{\circ}\mathrm{C}$  for printed the PLA/CF 3D printing.

Generally, mechanical performance of the FDM 3D printing depends on the layer adhesion in the products. Nevertheless, mechanical properties of composite materials in the FDM 3D printing were improved but limited in the layer adhesion [1,16,22]. To clarify the layer adhesion and interfacial adhesion of the composites 3D printing, rheological studied and dynamic mechanical analysis are used to understand the interfacial adhesion, the interlayer adhesion and properties of polymer composites and the FDM 3D printing [3,4,10,19,23-29]. Aw, et al. [19] studied the effect of printing parameters on tensile, dynamic mechanical, and thermoelectrical properties of FDM 3D printed conductive ABS (CABS)/zinc oxide  $(\mathrm{ZnO})$  composites. An increment of the storage modulus implied the improvement of stiffness and informed good interfacial adhesion between fillers and the matrix in CABS/ZnO composites FDM 3D printing. While the loss modulus and the damping properties decreased with increasing the infill density [19]. Thermal properties and dynamic mechanical properties of PLA/mica composites were reported by Kim, et al. [27]. Mica was the initial nuclei for PLA crystallization and might become the anchored molecules to enhance the interfacial adhesion through mechanical interlocking. Kunjappan, et al. [28] discussed on the reinforcement efficiency factor, degree of entanglement, and the effectiveness of multiwall carbon nanotube (MWCNT) to inform the interfacial adhesion and the effectiveness of MWCNT on properties of poly(trimethylene terephthalate)/polyethylene blend composites. Jyoti, et al. [26] applied the dynamic mechanical analysis to clarify the effectiveness of the MWCNT to reinforce MWCNT/ABS composites. Hence, the rheological behavior, the dynamic mechanical properties, the degree of entanglement density, the adhesion factor and the Cole-Cole analysis are carried out to clarify the flow behavior, the phase structure, the interfacial adhesion and the layer adhesion in the FDM 3D printing of polymer composites. This information would be a benchmark to development polymer composites and printing conditions for superior properties of the polymer composites FDM 3D printing.

In this research, the roles of additives and the printing bed temperatures on flow behavior, the layer adhesion, thermal properties, mechanical performance, and failure behavior in PLA composites FDM 3D printing were investigated. The phase structure of the PLA composites was analyzed by the Cole-Cole analysis. Dynamic mechanical properties were discussed in term of molecular entanglement, adhesion factor, effectiveness coefficient and reinforcement efficiency factor to interpretation the layer adhesion, the interfacial adhesion, and elucidate mechanical performance and failure characteristic of the PLA composites FDM 3D printing.

# 2. Materials and Methods

# 2.1. Filaments and Sample Preparation

Four types of commercially available poly(lactic acid) (PLA) filaments including neat PLA and PLA composites with particulate filler, carbon fiber, and copper particle were used as received. The formulations and the processing of the filaments are owned by the manufacturer. Table 1 tabulated compositions and designations of the PLA composites filaments in this study. Since the formulations and the processing of the filaments are owned by the manufacturer, the characteristic of the additives in the filaments was observed by scanning electron microscope (SEM) and solid residual of additives and thermal stability were measured by thermogravimetric analysis (TGA). The contents of particulate filler (P), carbon fiber (CF) and copper particle (Cu) were characterized by thermogravimetric analyzer, which were about  $5\mathrm{wt.\%}$ ,  $14\mathrm{wt.\%}$  and  $66\mathrm{wt.\%}$ , respectively, as presented in Table 1.

Table 1. Designation and composition of PLA filaments.  

<table><tr><td>Designation</td><td>Polymer</td><td>Additive</td><td>Residual1(%)</td><td>Td5%1(°C)</td><td>Tdpeak1(°C)</td></tr><tr><td>PLA-N</td><td>PLA</td><td>-</td><td>0.0</td><td>317.6</td><td>353.0</td></tr><tr><td>PLA-P</td><td>PLA</td><td>Particulate filler</td><td>5.2</td><td>317.3</td><td>352.5</td></tr><tr><td>PLA-CF</td><td>PLA</td><td>Carbon fiber</td><td>14.0</td><td>305.4</td><td>348.9</td></tr><tr><td>PLA-Cu</td><td>PLA</td><td>Copper particle</td><td>66.4</td><td>311.4</td><td>343.3</td></tr></table>

$^{1}$  Residual content at  $500^{\circ}\mathrm{C}$  and decomposition temperature  $(\mathrm{T_{d5\%}}$  and  $\mathrm{T_{dpeak}})$  from TGA.

The filaments were printed by the FDM 3D printing (da Vinci 1.0 Pro, XYZprinting, Inc., New Taipei City, Taiwan) to bar samples (60 mm long, 10 mm wide, and 2 mm thick) and dumbbell samples (75 mm long, 5 mm wide, and 2 mm thick) in XZ-directions. The nozzle was 0.4 mm-diameter and set at temperature of  $210^{\circ}\mathrm{C}$ . The printed bed temperatures were varied at  $45^{\circ}\mathrm{C}$  and  $60^{\circ}\mathrm{C}$ . Figure 1 depicts the printing direction, the size of the dumbbell sample and the cross sectional for morphology observation. The conditions for 3D printing are summarized in Table 2 [5,11,22].

![](images/76a0c5731ef5df7a20155fd29c2231fa6984fa8c62740fd1853e5e6b50e8c629.jpg)  
(a)

![](images/770f60779f491bf215f41dce8fbdea7ba2aab027b5368806d849decadaf86ec6.jpg)  
(b)

![](images/fcd5abd776752e9fcb1f90fb42373b0d4e2a94ceca8260c8e4395ef61f42ba54.jpg)  
(c)  
Figure 1. 3D printing sample preparation: (a) Printing direction; (b) size of dumbbell specimen; and (c) cross sectional for morphology observation.

Table 2. Conditions of FDM 3D printing.  

<table><tr><td>Parameter</td><td>FDM 3D Printing Condition</td></tr><tr><td>Nozzle temperature</td><td>210 °C</td></tr><tr><td>Bed temperature</td><td>45 °C and 60 °C</td></tr><tr><td>Printing speed</td><td>25 mm/s</td></tr><tr><td>Layer height</td><td>0.2 mm</td></tr><tr><td>Shell thickness</td><td>2 layers</td></tr><tr><td>Raster angle</td><td>0°</td></tr><tr><td>Infill type</td><td>Rectilinear</td></tr><tr><td>Infill density</td><td>100%</td></tr></table>

![](images/9be2fc6c6312e5e37741c70c7fbc750cbc95552eb0bf947019bd4f3de6a66a9e.jpg)  
(a) PLA-N

![](images/bc7caa1e5ec862fae353b46d998f4f2a8504a86699dc8e71ed0a0b7fe27ffcc0.jpg)  
Figure 2 shows photographs of bar and dumbbell 3D printed samples of PLA composites printed at bed  $60^{\circ}\mathrm{C}$ .  
(b) PLA-P  
Figure 2. Bar (top) and dumbbell (bottom) 3D printed samples from bed temperature  $60^{\circ}\mathrm{C}$ : (a) PLA-N; (b) PLA-P; (c) PLA-CF; and (d) PLA-Cu.

![](images/7b9c5f30d266db8ebbc40bd1d24d6a04a927bfe279d612c8eca2a9921e01c844.jpg)  
(c) PLA-CF

![](images/9d0969c553261517595c9139f93019a5e6230ff88ffec8c29e3fea38cc0e57f6.jpg)  
(d) PLA-Cu

In addition, the filaments were cut and compression-molded to  $2\mathrm{mm}$ -thick sheets by a compression molding machine (Mini Test Press MP-WNH, Toyo Seiki Seisaku-sho, Ltd., Tokyo, Japan) at temperature of  $200^{\circ}\mathrm{C}$  with pressure  $10\mathrm{MPa}$  for  $5\mathrm{min}$ .

The samples designations such as PLA-N filament, compression molded sheet, 3D printed samples at bed  $45^{\circ}\mathrm{C}$  and at bed  $60^{\circ}\mathrm{C}$  are referred as PLA-N-F, PLA-N-C, PLA-N-B45 and PLA-N-B60, respectively.

# 2.2. Characterization

# 2.2.1. Morphology

Characteristic of the additives used in the filament was observed from the compression molded sheet of the filaments by SEM (JSM-6510, JEOL Ltd., Tokyo, Japan). Cross sectional morphology of the 3D printed samples as shown in Figure 1c was observed from cryogenic fractured surfaces and tensile fractured surfaces by an optical microscope (VHX950F, Keyence Corporation, Osaka, Japan) and SEM (TM3030plus, Hitachi High-Technologies Corporation, Tokyo, Japan). The surfaces of SEM samples were coated with platinum and observed at an accelerated voltage of  $5\mathrm{kV}$ .

# 2.2.2. Rheological Properties

Rheological properties were tested with the compression molded sheets of the filaments. Samples were conducted by a rotary rheometer (Modular Compact Rheometer, MCR 302, Anton Paar GmbH, Graz, Austria) using a  $25\mathrm{mm}$  parallel plate. The temperature was set at  $210^{\circ}\mathrm{C}$ . The oscillatory mode was set with frequency ranges from 0.01 to  $1000~\mathrm{rad / s}$  with strain rate of  $1.0\%$ .

# 2.2.3. Thermal Properties

Thermal stability and the residual of the additives of the filaments were analyzed by a thermogravimetric analyzer (TGA, Q50, TA Instruments, New Castle, DE, USA). The weight of sample was about  $10\mathrm{mg}$ . The temperature was set from the ambient to  $600^{\circ}\mathrm{C}$  at the heating rate of  $10^{\circ}\mathrm{C / min}$  under nitrogen atmosphere.

Thermal properties and crystallization behavior of the filaments, the compression molded sheets and the 3D printing samples were characterized using a differential scanning calorimeter (DSC, Q200, TA Instruments, New Castle, DE, USA) under nitrogen atmosphere. The 3D printing samples were cut from the center of dumbbell specimens. Samples about  $5\mathrm{mg}$  were sealed in aluminum pan. The DSC analysis was run on heat-cool-heat cycles set from  $-70^{\circ}\mathrm{C}$  to  $200^{\circ}\mathrm{C}$  at the heating and cooling rates of  $10^{\circ}\mathrm{C / min}$ . The cycle was

held isothermally  $5\mathrm{min}$  before running the cycle. Crystallinity of PLA in the samples was calculated as described in the literature [5,22] by the following equation.

$$
X _ {c} (\%) = \frac {\left(\Delta H _ {m} - \Delta H _ {c c}\right)}{\Delta H _ {f} ^ {0} \times W _ {P L A}} \times 100 \tag{1}
$$

where  $X_{c}$  is the percentage of crystallinity,  $\Delta H_{m}$  is the enthalpy of melting,  $\Delta H_{cc}$  is the enthalpy of cold crystallization,  $\Delta H_{f}^{0}$  is 93.7 J/g for the enthalpy of fusion of fully crystalline PLA [5], and  $W_{PLA}$  is the weight fraction of PLA in the filaments.

# 2.2.4. Dynamic Mechanical Properties

Dynamic mechanical analysis was carried out by the RSA G2 solids analyzer (TA Instruments, New Castle, DE, USA). The bar specimens (30 mm long, 6 mm wide, and 2 mm thick) from the compression molded sheets and the 3D printings were run at 3-point bending mode. The condition was set from room temperature to  $120^{\circ}\mathrm{C}$  at the heating rate of  $3^{\circ}\mathrm{C / min}$  and frequency of  $1\mathrm{Hz}$ . Storage modulus  $(\mathrm{E}^{\prime})$ , loss modulus  $(\mathrm{E}^{\prime \prime})$  and Tan  $\delta$  were recorded.

# 2.2.5. Mechanical Properties

Flexural and tensile properties were performed using a universal testing machine (Strograph VGS1-E, Toyo Seiki Seisaku-sho, Ltd., Tokyo, Japan). Flexural testing was done according to ISO 178 with bar specimens  $(n = 3)$  at span length of  $32\mathrm{mm}$  and testing speed of  $2\mathrm{mm / min}$ . Tensile testing was carried out according to ISO 527-2 type 1 BA with dumbbell specimens  $(n = 5)$  at gauge length of  $30\mathrm{mm}$  and testing speed of  $10\mathrm{mm / min}$ .

# 3. Results and Discussion

# 3.1. Morphology of the Compression Molded Sheet of the PLA Filaments

Figure 3 depicts SEM images of cryogenic fractured surfaces of the compression molded sheet of the PLA filaments. The fractured surface of the PLA-N-C was smooth as indicated its brittleness as presented in Figure 3a. Figure 3b-d show morphology and characteristic of the additives on the PLA matrix. The particulate fillers in the PLA-P-C were good distribution and dispersion on the PLA matrix. The SEM image of the PLA-CF-C showed good adhesion of the CF on the matrix, which no CF fiber pulled out. Large copper particles and a kind of rubbery dispersed phase can be observed in the PLA-Cu-C. These SEM images could be encouraged the rheological properties, thermal properties, dynamic mechanical properties, and mechanical performance of the PLA composites 3D printings.

![](images/e343532ef1616009483461597211fa34fcdf77c436c4338ca4a41f4366e00df1.jpg)  
(a) PLA-N-C

![](images/d81c31631db160ae919dbba2d2d3f2beeb3ee8041304add05de14e843a719b6e.jpg)  
(b) PLA-P-C

![](images/0abbe6937d2d88057029a396aa1a1a593a96862c28eba5e19e6ea2a49134395d.jpg)  
(c) PLA-CF-C  
Figure 3. SEM images of cryogenic fractured surfaces of PLA filaments compression molded sheets: (a) PLA-N-C; (b) PLA-P-C; (c) PLA-CF-C; and (d) PLA-Cu-C.

![](images/ee34ad4a5d4af352c23ec96b8f61bbc3e17931c58a3000841ef68dd2311a4894.jpg)  
(d) PLA-Cu-C

# 3.2. Rheological Properties

Rheological behaviors of the PLA and PLA composites were carried out to understand their flowability and viscoelastic properties under shearing since molten filaments were extruded passed through the hot nozzle. Rheological properties provide information of molecular entanglement and molecular relaxation, layer stability, and guideline of layer adhesion for FDM 3D printability [5,10,11].

Flow curves of the compression molded sheets of PLA composites filaments at  $210^{\circ}\mathrm{C}$  are shown in Figure 4a for shear stress and Figure 4b for complex viscosity as a function of shear rate. At low shear rate, the shear stress and the complex viscosity of PLA-Cu and PLA-CF were higher than PLA-N and PLA-P. It was considered that CF and Cu inhibit movement of polymer molecule that raised their stress and viscosities. The high complex viscosity informs interaction between CF and Cu with the PLA matrix and increased elastic deformation and molecular entanglement of PLA-CF and PLA-Cu than PLA-N and PLA-P at the low shear rate. All filaments were pseudoplastic flow behavior. At high shear rate, the shear stress and the complex viscosity of all filaments revealed the shear thinning and the values were comparable regardless with the incorporation of additives. These indicated similarity of the PLA mainly matrix in the composite filaments [30]. Figure S1 presents the complex viscosity as a function of angular frequencies, which the viscosity characteristics of the PLA-N and PLA-P were also observed in Benwood et al. [5]. This research reported the complex viscosity of PLA filaments FDM 3D printing at various temperatures. From the rheological study, it was used to confirm the change of viscosity in the printing nozzle and informed the dimensional accuracy. Higher viscosity and proper control printing at  $210^{\circ}\mathrm{C}$  with bed temperature of  $60^{\circ}\mathrm{C}$  were optimized for high dimensional accuracy between the successive of voids between the layers in the 3D printings [5].

![](images/6906088a26e7a899250c1dde9f703db47cce265d5c75e216abc47d55e904921c.jpg)  
(a)  
Figure 4. Flow curves of PLA filaments at  $210^{\circ}\mathrm{C}$ : (a) shear stress and (b) complex viscosity.

![](images/a843f5f5dbcb763c2c2fa5281af352700ef5f001ccdf621483dcd548a28b0db2.jpg)  
(b)

The power-law model as presented in Equation (2) is determined the flow behavior to identify 3D printing layer and dimensional stability [11,31], where  $\tau$  is shear stress,  $\dot{\gamma}$  is shear rate, K is consistency index, and  $n$  is power-law index, which were estimated by the power regression.

$$
\tau = \mathrm {K} \dot {\gamma} ^ {n} \tag {2}
$$

Table 3 summarizes viscosity, the power-law index and the consistency index of the filaments at  $210^{\circ}\mathrm{C}$ . The viscosity  $(\eta)$  values at two ranges of shear rates that related to flow behavior of the 3D printing filaments. The  $\eta$  values at  $0.2\mathrm{s}^{-1}$  and  $0.01\mathrm{s}^{-1}$  informed viscous flow of molten filament passing through the hot nozzle and during printed layer-by-layer, respectively [11]. It was surprisingly that the molten PLA composites have lower viscosities than the neat PLA. The viscosities of all molten filaments increased since the shear rate of the molten filaments decreased after extruded from the nozzle then layer deposition. The PLA-Cu has the highest viscosity along the layer deposition, which the layer might collapse

from the high viscosity. The power-law index (n) of PLA-N and PLA-P were 0.91 and 0.95, which closed to the Newtonian flow  $(n = 1)$ . On the contrary, PLA-CF and PLA-Cu have  $n < 1$ , which informed the shear thinning behavior. The consistency index (K) can be referred to the overall viscosity of the PLA composites filaments. The K values of the filaments were about 200–400 Pa·s. Nguyen, et al. [10] reported the window suggested for attaining good 3D printability by the shear rate about  $190~\mathrm{s}^{-1}$  to  $3000~\mathrm{s}^{-1}$  and the viscosity about 70 Pa·s to 500 Pa·s. In addition, the shear thinning with high viscosity could obtain the shape accuracy as reported in the literature [11]. Hence, the results confirmed that the PLA composites filaments would perform good printability.

Table 3. Complex viscosity and power-law index of PLA filaments at  ${210}^{ \circ  }\mathrm{C}$  .  

<table><tr><td>Sample</td><td>η at γ 0.2 s-1(Pa·s)</td><td>η at γ 0.1 s-1(Pa·s)</td><td>K (Pa·s)</td><td>n</td><td>Power Regression (R2)</td></tr><tr><td>PLA-N</td><td>555.5</td><td>694.6</td><td>381.2</td><td>0.91</td><td>0.99</td></tr><tr><td>PLA-P</td><td>426.2</td><td>464.7</td><td>324.2</td><td>0.95</td><td>0.99</td></tr><tr><td>PLA-CF</td><td>313.7</td><td>474.5</td><td>215.2</td><td>0.76</td><td>0.99</td></tr><tr><td>PLA-Cu</td><td>305.3</td><td>1377.5</td><td>222.1</td><td>0.52</td><td>0.94</td></tr></table>

Figure 5 displays storage and loss modulus under shearing of the PLA filaments. From the storage modulus  $(\mathrm{G}^{\prime})$ , the sudden drop of the  $\mathrm{G}^{\prime}$  at low frequency of PLA-N and PLA-P indicated loss of elasticity, which implied molecular deterioration of the PLA matrix when processed at long time [22]. The storage moduli of the PLA composites were higher than PLA-N at the low frequency. It was attributed to interaction and good distribution of additives in the PLA matrix. In addition, the high values of  $\mathrm{G}^{\prime}$  informed elastic deformation and molecular entanglement of PLA-CF and PLA-Cu at low frequency. It can be noted that the  $\mathrm{G}^{\prime}$  and the loss modulus  $(\mathrm{G}^{\prime \prime})$  of PLA-Cu were equally at low frequency. It might inform the combination of solid-liquid transition behavior, which affected on molecular relaxation of the PLA-Cu filament [30]. From the loss modulus, all filaments were similarly in viscous behavior of the PLA matrix. Hence, the incorporation of the additives would stabilize molten PLA composites filaments during 3D printing [11].

![](images/b602b8a31a4f9f61034625e6836387966b9863b99c3b6307ef8ee092c4d1a438.jpg)  
Figure 5. Storage modulus and loss modulus of PLA filaments.

# 3.3. Thermal Properties and Crystallization Behavior

Figure 6 illustrates DSC thermograms of the PLA composites filaments from the first heating, the cooling and the second heating cycles to investigate the effect of additives on thermal properties of the PLA composites filaments. The thermograms from the first and the second heating cycles display glass transition temperature  $(\mathrm{T_g})$ , cold crystallization temperature  $(\mathrm{T_{cc}})$ , and melting temperature  $(\mathrm{T_m})$  of PLA and the crystallization temperature

$(\mathrm{T_c})$  at the cooling cycle.  $\mathrm{T_g}$  of the PLA matrix around  $60 - 64^{\circ}C$  can be clearly seen from the first heating while it was broad in the second heating as the PLA could be crystallized after removed thermal history and controlled the cooling rate [27]. An exothermic area at the heating cycles informed the  $\mathrm{T_{cc}}$  that indicated slow crystallized and imperfect crystal of PLA matrix [23]. An endothermic peak around  $165 - 170^{\circ}C$  of the first and the second heating cycles indicates  $\mathrm{T_m}$  of the PLA matrix. The exothermic peaks of the cooling cycles are clearly seen in PLA-N, PLA-P, and PLA-Cu. The higher  $\mathrm{T_c}$  and sharp intensities of the  $\mathrm{T_c}$  and the  $\mathrm{T_m}$  of the second heating peaks in the PLA-P and the PLA-Cu implied an improvement of PLA crystallization from the adding of particulate filler and Cu. On the other hand, the appearance of  $\mathrm{T_{cc}}$  in the PLA-CF informed that CF retarded the crystallization of PLA. Nevertheless, semicrystalline PLA in the PLA-CF samples was crystallized, which small  $\mathrm{T_c}$  of the PLA-CF can be seen when enlarging the cooling cycles as shown in Figure S2. It can be noted that PLA-Cu filament might be modified for improved filler distribution and flowability by rubbery additive, which can be observed the  $\mathrm{T_g}$  around  $0^{\circ}C$  in Figure 6d. This result could be confirmed the rubbery dispersed phase that observed in the morphology of the PLA-Cu-C in Figure 3d. The thermal properties of the PLA filaments were discussed with compression molded sheets and 3D printed samples.

![](images/ca7647c83082fcc649530ce701ee36f1caf919977798fc32ce6706e9f4fa810f.jpg)  
(a)

![](images/3f5a0a67ead8a9c247ea6f748c94db3efe34086bf78cbbc9b0dfd1a949893a16.jpg)  
(b)

![](images/7fded2dcd0e4ad3cee2f8666559d598e5e030576708f120547cdde8ea9741255.jpg)  
(c)

![](images/9cd057b0bac5e891b5805fc010f54f39942e0df011208c1280d1f3194f76b56e.jpg)  
(d)  
Figure 6. DSC thermograms of PLA filaments: (a) PLA-N; (b) PLA-P; (c) PLA-CF; and (d) PLA-Cu.

Figure 7 depicts a comparison of the first heating DSC thermograms of the compression molded sheets, the 3D printed samples and their filaments to investigate the effect of thermal history from the additives and the processing on thermal characteristic of PLA. Table 4 summaries thermal properties of all samples.  $\mathrm{T_g}$  values of the filaments were about  $64^{\circ}\mathrm{C}$ . Except PLA-Cu-F that was about  $62^{\circ}\mathrm{C}$ , which was due to the rubbery additive in this filament. The  $\mathrm{T_g}$  values of the 3D printed samples were shifted to lower temperature

as compared to the filaments and the compression molded sheets. It might be due to polymer mobility during the 3D printing process. However, the  $\mathrm{T_g}$  of PLA-Cu 3D printings slightly shifted to higher temperature, which high amount of Cu might limit the mobility of polymer in the 3D printing. However, faster cooling rate in the compression molded reflected in higher amorphous region that indicated by larger intensities of the  $\mathrm{T_g}$  and the  $\mathrm{T_{cc}}$  area and lower in crystallinity as compared to the filaments and the 3D printed products. The incorporation of the additives and the increasing of the bed temperatures improved crystallization of the PLA matrix, which indicated by a decreasing of the  $\mathrm{T_{cc}}$  and an increasing of crystallinity as tabulated in Table 4. The improvement of the PLA crystallization in the 3D printed products was more pronounced in PLA-N and PLA-P, especially when printed at bed  $60^{\circ}\mathrm{C}$  that would imply high stiffness of PLA-N-B60 and PLA-P-B60 samples. The  $\mathrm{T_m}$  values of PLA in the compression molded sheets and the 3D printed samples were about  $166 - 170^{\circ}\mathrm{C}$  depend on PLA crystallization. The decreasing of  $\mathrm{T_m}$  in the first heating cycle was due to crystal formation affected from the additives and the processing conditions. The crystallinity of the filaments and the 3D printing samples were higher than the compression molded sheets. It was attributed to the molecular orientation of PLA during extrusion process.

![](images/0db0a7083b30067bf1a6fa0901b200e5cba85d7bb12dd541e4ed2119bcb722cb.jpg)  
(a)

![](images/54ba47d75b18d17ec930be48bc6c638b2b2f94f2b53d73fe6a7dfab5d06d6ab4.jpg)  
(b)

![](images/9de131f19092ad4869a810c59c3169f1f2bfdf1f26d1114e1a6147c4a0cd2026.jpg)  
(c)

![](images/c7f3de706480c4ae1ef735d8a7107031a4c392024fd2d7e7c345e86b65750552.jpg)  
(d)  
Figure 7. DSC thermograms of the first heating cycle of compression molded sheet and 3D printed samples: (a) PLA-N; (b) PLA-P; (c) PLA-CF; and (d) PLA-Cu.

Table 4. Thermal properties and crystallinity of filaments, compression molded sheets, and 3D printed samples.  

<table><tr><td rowspan="2">Sample</td><td colspan="4">DSC First Heating Cycle</td><td colspan="3">DSC Cooling Cycle</td><td colspan="3">DSC Second Heating Cycle</td></tr><tr><td>Tg1 (°C)</td><td>Tcc1 (°C)</td><td>Tm1 (°C)</td><td>Xc1 (%)</td><td>Tc (°C)</td><td>ΔHc (J/g)</td><td>Tg2 (°C)</td><td>Tcc2 (°C)</td><td>Tm2 (°C)</td><td>Xc2 (%)</td></tr><tr><td>PLA-N-F</td><td>64.1</td><td>101.0</td><td>170.1</td><td>8.5</td><td>112.6</td><td>37.8</td><td>60.3</td><td>-</td><td>165.0, 168.8</td><td>35.8</td></tr><tr><td>PLA-N-C</td><td>64.1</td><td>106.1</td><td>168.3</td><td>3.7</td><td>108.2</td><td>30.6</td><td>61.7</td><td>99.5</td><td>163.8, 168.6</td><td>34.2</td></tr><tr><td>PLA-N-B45</td><td>60.6</td><td>99.9</td><td>167.9</td><td>5.3</td><td>111.1</td><td>32.7</td><td>62.0</td><td>-</td><td>164.3, 168.5</td><td>35.5</td></tr><tr><td>PLA-N-B60</td><td>61.8</td><td>95.2</td><td>167.3</td><td>11.6</td><td>112.4</td><td>32.6</td><td>61.9</td><td>-</td><td>164.1, 168.3</td><td>34.6</td></tr><tr><td>PLA-P-F</td><td>64.0</td><td>97.3</td><td>169.6</td><td>7.7</td><td>124.0</td><td>36.9</td><td>62.4</td><td>-</td><td>166.4</td><td>42.5</td></tr><tr><td>PLA-P-C</td><td>63.4</td><td>97.0</td><td>168.3</td><td>5.8</td><td>124.2</td><td>37.7</td><td>61.8</td><td>-</td><td>166.5</td><td>42.7</td></tr><tr><td>PLA-P-B45</td><td>60.5</td><td>96.4</td><td>167.3</td><td>8.3</td><td>123.7</td><td>36.7</td><td>63.2</td><td>-</td><td>166.0</td><td>41.8</td></tr><tr><td>PLA-P-B60</td><td>60.9</td><td>95.0</td><td>167.2</td><td>10.5</td><td>123.7</td><td>36.7</td><td>62.5</td><td>-</td><td>165.7</td><td>42.2</td></tr><tr><td>PLA-CF-F</td><td>64.6</td><td>90.4</td><td>167.2</td><td>11.8</td><td>91.3</td><td>0.8</td><td>60.6</td><td>102.9</td><td>166.7</td><td>9.2</td></tr><tr><td>PLA-CF-C</td><td>62.7</td><td>90.9</td><td>166.2</td><td>8.4</td><td>90.2</td><td>2.0</td><td>60.2</td><td>99.4</td><td>166.3</td><td>9.7</td></tr><tr><td>PLA-CF-B45</td><td>60.9</td><td>92.1</td><td>165.4</td><td>9.2</td><td>91.5</td><td>1.5</td><td>60.9</td><td>103.0</td><td>166.3</td><td>8.8</td></tr><tr><td>PLA-CF-B60</td><td>61.1</td><td>93.1</td><td>165.5</td><td>9.0</td><td>92.1</td><td>1.0</td><td>60.4</td><td>103.1</td><td>166.2</td><td>8.3</td></tr><tr><td>PLA-Cu-F</td><td>61.8</td><td>89.0</td><td>166.4</td><td>11.2</td><td>126.0</td><td>10.7</td><td>61.9</td><td>-</td><td>164.8</td><td>30.4</td></tr><tr><td>PLA-Cu-C</td><td>62.8</td><td>89.7</td><td>166.3</td><td>9.1</td><td>126.9</td><td>11.3</td><td>61.8</td><td>-</td><td>164.5</td><td>31.1</td></tr><tr><td>PLA-Cu-B45</td><td>63.4</td><td>92.1</td><td>166.4</td><td>11.6</td><td>126.6</td><td>11.3</td><td>62.0</td><td>-</td><td>164.7</td><td>30.1</td></tr><tr><td>PLA-Cu-B60</td><td>62.8</td><td>92.2</td><td>166.4</td><td>11.1</td><td>126.3</td><td>11.0</td><td>62.1</td><td>-</td><td>164.7</td><td>30.9</td></tr></table>

According to the 3D printing process, there was much accumulation of heat when printed at higher bed temperature. Then, PLA might have smaller crystal formation from higher cooling rate when using higher bed temperature as compared to the lower one [18]. In the second heating after controlled cooling process, the  $\mathrm{T_g}$  values were around  $62^{\circ}\mathrm{C}$  in all samples, which were assumed similarity of the PLA matrix in the neat PLA and the PLA composites filaments. The PLA-N samples presented two melting peaks while the other showed one  $\mathrm{T_m}$  at  $165 - 166^{\circ}\mathrm{C}$ . It was corresponding to difference of crystal sizes in the pristine PLA-N during crystallization [32]. The  $\mathrm{T_m}$  value in the second heating of each sample was unchanged, which implied no degradation of the PLA matrix after processing. The higher  $\mathrm{T_c}$  of PLA-P and PLA-Cu than PLA-N informed that the particulate filler and the Cu acted as heterogeneous nucleating sites and enhanced the crystallization of the PLA matrix [5,27]. It can be noted that the  $\mathrm{T_c}$  of the samples were hinted for layer solidification in the 3D printing process [22]. Higher  $\mathrm{T_c}$  allows faster solidification that might restrict layer adhesion in the 3D printing. Hence, controlling in thermal and crystallization properties of PLA would design its printing quality and mechanical performance of the 3D printed products.

# 3.4. Dynamic Mechanical Properties

Dynamic mechanical properties inform the viscoelastic properties of polymers, which can be used to understand phase transition, molecular mobility and damping property of polymer, and compatibility as well as interfacial adhesion of polymer blends and composites [24-27,33]. Additionally, the dynamic mechanical properties can be implied the layer adhesion in the 3D printing products [19,34]. The effects of additives and processing conditions on the dynamic mechanical properties of the PLA composites compression molded sheets and the 3D printed samples are illustrated in Figure 8. The storage modulus  $(\mathrm{E}^{\prime})$ , loss modulus  $(\mathrm{E}^{\prime \prime})$  and Tan  $\delta$  values of the samples are summarized in Table 5. Phase transitions of the materials according to molecular mobility from glassy region, glass transition region, rubbery region, and flow region can be indicated from changing of the  $\mathrm{E}^{\prime}$  values at elevated temperatures. The  $\mathrm{E}^{\prime}$  decreased when increasing temperature and sudden drop at the glass transition temperature toward the rubbery stage and increased viscous and chain mobility [25,26]. The compression molded of the PLA-N-C and the PLA-P-C lost their stiffness around  $70^{\circ}\mathrm{C}$  whereas the stiffness could be recovered in the

other compression molding and the 3D printing samples from the cold crystallization [32]. The incorporation of the particulate filler and the Cu particle improved the crystallization of the PLA and rose the  $\mathrm{E}^{\prime}$  at elevated temperature. Additionally, the  $\mathrm{E}^{\prime}$  increased when increasing bed temperature from the crystallinity improvement. Storage moduli of the compression molded PLA-N-C, PLA-P-C and PLA-Cu-C were higher than their 3D printed samples because of good adhesion and the interaction between the additives and the PLA matrix. The PLA-CF-C, PLA-CF-B45 and PLA-CF-B60 showed the maximum  $\mathrm{E}^{\prime}$  values, which were stiffer as compared to the other due to the reinforcement and stiffness of the CF. In addition, the anisotropic orientation of the CF along the extruded 3D printing yielded higher  $\mathrm{E}^{\prime}$  than the PLA-CF-C one. Nevertheless, the Cu particles declined the  $\mathrm{E}^{\prime}$  of the 3D printed PLA-Cu-B45 and PLA-Cu-B60, which might be due to the rubbery phase and limited layer adhesion. The  $\mathrm{E}^{\prime}$  along the rubbery state can be informed thermal resistance of the polymers indicated by a shift of the  $\mathrm{E}^{\prime}$  to higher temperature. From Figure 8a and the  $\mathrm{E}^{\prime}$  values at  $60^{\circ}\mathrm{C}$  in Table 5, the 3D printed samples exhibited higher thermal resistance and harder than the compression molded sheets. Additionally, the PLA-N-C and PLA-P-C lost their stiffness at temperatures over  $80^{\circ}\mathrm{C}$ , which was probably attributed to highly amorphous state of the compression molded PLA-N-C and PLA-P-C. It can be confirmed that the incorporation of the additives and the 3D printing process enhanced the thermal resistance, the elasticity, and the stiffness of the 3D printed samples [11,19,33].

Figure 8b displayed  $\mathrm{E}''$  curve of the PLA composites compression molded, and the 3D printed samples. The  $\mathrm{E}''$  support information of viscous response of materials, energy dissipation and related to relaxation process [23,26]. The  $\mathrm{E}''$  peaks of the 3D printed samples shift to higher temperatures. Higher  $\mathrm{E}''$  values indicated more energy dissipation, which was attributed to an increment of internal friction in composites.  $\mathrm{E}''$  of the PLA-P and PLA-CF composites were higher than the neat PLA. Akindoyo, et al. [23] reported that higher  $\mathrm{E}''$  of the composites than neat PLA could be due to the higher segmentation of chains in the PLA matrix, which the reinforcing fillers might have hindered chain relaxations within the composite and larger number of energy dispersing spots formed by interfacial bonding.

The damping property and the glass transition temperature of the samples were determined by Tan  $\delta$  as presented in Figure 8c. All compression molded exhibited higher Tan  $\delta$ , which the energy was more dissipate than the 3D printed samples. The damping property of the 3D printed samples improved when increasing the bed temperature that materials would have more potential to store energy than dissipation [19].

The storage modulus and the Tan  $\delta$  values were used to investigate the degree of entanglement density  $(N)$ , the adhesion factor  $(A)$ , the effectiveness coefficient  $(C)$ , and the reinforcing factor  $(r)$  of the fillers in the PLA composites samples. All parameters are calculated from Equations (3)-(6) [23,25,26,28,29,34] and the results tabulate in Table 5.

![](images/ca091b79f768ea53d771cf7cdab68a8223d0ea41c9f676d2ee2316a3a0afc450.jpg)

![](images/af4b701c78c0f1bd3efcd6a5cc9229f034f169d56d056ae6a7a3b7c404c73538.jpg)

![](images/c3da59c629e74ed3a872db1ca9a62a2ccbd8ad916d67c2115b6d53c01c516613.jpg)

![](images/42c42377b3a9b417d6d7069bd1add1b37634ca34e031fd96d0427fc91b6ba04e.jpg)

![](images/c81594fd635248925cc06a27c634626569c6b7e5947b74e9b5046c752da6a826.jpg)

![](images/daca7dbe5257de7c6c6360f6a8364b05572295778331efbab59f06258b502c62.jpg)

![](images/03a6119bb3f530f8d7d025fe84b6f7ade607725ba879fbabfb108d5ce40a1644.jpg)

![](images/0b34c3cb754f814e98c6cc933e5bfd3c85f15708a44519b56b3b6161382d60c6.jpg)

![](images/1b711a46292fb0a26e7a07bce4c31ca5906c048e8f6b338b9f1c32fd246bd7d6.jpg)

![](images/5ccc31e0f5a8a3a11661cf5f8bda55f8ecc17b74e2fd5370c519c87029cdadae.jpg)  
(a)

![](images/ecca2119f4c57f0445beb4844357877dafa1b332808eba4481107b5c8adc59e2.jpg)  
(b)

![](images/a942aa77dae1e562f70fc702b353c01398d28376b1b366f901cfb1a58edd3d1b.jpg)  
(c)  
Figure 8. Storage modulus, loss modulus and Tan  $\delta$  of compression molded sheets and 3D printed samples: (a) Storage modulus; (b) Loss modulus; and (c) Tan  $\delta$ .

Table 5. Dynamic mechanical properties of compression molded sheets and 3D printed samples.  

<table><tr><td>Sample</td><td>E&#x27; (GPa) at 40 °C</td><td>E&#x27; (GPa) at 60 °C</td><td>E&#x27;&#x27; (MPa)1</td><td>Tg, Tan δ2 (°C)</td><td>Tan δ2</td><td>N (mol/m3)</td><td>A</td><td>C</td><td>r</td></tr><tr><td>PLA-N-C</td><td>2.91</td><td>0.48</td><td>0.38</td><td>65.6</td><td>2.33</td><td>2.89 × 104</td><td></td><td></td><td></td></tr><tr><td>PLA-N-B45</td><td>2.65</td><td>0.46</td><td>0.35</td><td>65.6</td><td>1.74</td><td>2.76 × 104</td><td></td><td></td><td></td></tr><tr><td>PLA-N-B60</td><td>2.56</td><td>0.38</td><td>0.37</td><td>65.0</td><td>1.42</td><td>2.31 × 104</td><td></td><td></td><td></td></tr><tr><td>PLA-P-C</td><td>3.21</td><td>0.43</td><td>0.38</td><td>65.8</td><td>2.47</td><td>2.58 × 104</td><td>0.12</td><td>1.23</td><td>2.01</td></tr><tr><td>PLA-P-B45</td><td>2.66</td><td>1.07</td><td>0.45</td><td>64.4</td><td>0.76</td><td>6.41 × 104</td><td></td><td>0.43</td><td>0.02</td></tr><tr><td>PLA-P-B60</td><td>2.72</td><td>1.24</td><td>0.39</td><td>63.2</td><td>0.43</td><td>7.48 × 104</td><td></td><td>0.33</td><td>1.23</td></tr><tr><td>PLA-CF-C</td><td>5.00</td><td>0.77</td><td>0.75</td><td>64.8</td><td>1.77</td><td>4.63 × 104</td><td>-0.12</td><td>1.07</td><td>5.13</td></tr><tr><td>PLA-CF-B45</td><td>5.56</td><td>1.32</td><td>0.73</td><td>65.9</td><td>1.66</td><td>7.93 × 104</td><td></td><td>0.73</td><td>7.82</td></tr><tr><td>PLA-CF-B60</td><td>5.68</td><td>1.38</td><td>0.92</td><td>65.6</td><td>1.52</td><td>8.29 × 104</td><td></td><td>0.61</td><td>8.72</td></tr><tr><td>PLA-Cu-C</td><td>3.13</td><td>0.62</td><td>0.48</td><td>64.7</td><td>1.19</td><td>3.73 × 104</td><td>0.52</td><td>0.83</td><td>0.12</td></tr><tr><td>PLA-Cu-B45</td><td>1.57</td><td>0.74</td><td>0.26</td><td>65.2</td><td>0.65</td><td>4.45 × 104</td><td></td><td>0.37</td><td>-0.62</td></tr><tr><td>PLA-Cu-B60</td><td>1.74</td><td>0.99</td><td>0.26</td><td>64.5</td><td>0.41</td><td>5.96 × 104</td><td></td><td>0.26</td><td>-0.49</td></tr></table>

1 Peak of loss modulus. 2 Peak of Tan  $\delta$

The degree of entanglement density  $(N)$  can be calculated from the following [26,28]:

$$
N = \frac {E ^ {\prime}}{6 R T} \tag {3}
$$

where  $E^{\prime}$  is the storage modulus at the rubbery stage  $(60^{\circ}\mathrm{C})$ ,  $R$  is the universal gas constant  $(8.314\mathrm{J}\cdot \mathrm{mol}^{-1}\cdot \mathrm{K}^{-1})$ , and  $T$  is the absolute temperature at the rubbery stage.

The adhesion factor  $(A)$  can be described interfacial interaction and interaction between filler and the adhesion with the polymer matrix by measuring from damping factor as presented in the Equation (4) [23,26]:

$$
A = \frac {1}{\left(1 - V _ {f}\right)} \left(\frac {\tan \delta_ {c}}{\tan \delta_ {p}}\right) - 1 \tag {4}
$$

where  $V_{f}$  is volume fraction of the filler, and  $\tan \delta_{c}$  and  $\tan \delta_{p}$  is the maximum value of tan  $\delta$  peak of the composite and the neat polymer, respectively.

The effectiveness coefficient (C) can be calculated from the ratio of the storage modulus of the glassy stage  $(E_g^{\prime})$  and the rubbery stage  $(E_r^{\prime})$  between the composite and the neat polymer as presented in the following equation [23,25,26,29,34]:

$$
C = \frac {\left(\frac {E _ {8} ^ {\prime}}{E _ {r} ^ {\prime}}\right) \text {c o m p o s i t e}}{\left(\frac {E _ {8} ^ {\prime}}{E _ {r} ^ {\prime}}\right) \text {n e a t p o l y m e r}} \tag {5}
$$

The reinforcement efficiency factor  $(r)$  of the composite was investigated according to the rule of mixture from the Einstein equation [26,28].

$$
E _ {c} ^ {\prime} = E _ {m} ^ {\prime} \left(1 + r V _ {f}\right) \tag {6}
$$

where  $E_c'$  and  $E_m'$  are the storage modulus of the composite and the polymer matrix, respectively and  $V_f$  is volume fraction of the filler.

The degree of entanglement density would inform the effect of additives and the processing condition on molecular entangle in the neat polymer and the composites. The degree of entanglement density of the neat polymer was comparable in both compression molding and 3D printing processes. Higher content of the CF and the Cu obtained higher entanglement in the compression molded PLA-CF-C and PLA-Cu-C as compared to PLA-N-C and PLA-P-C. This information was correlated with the rheological properties. The entanglement of the PLA-N was comparable in the compression molded and the 3D printed specimen. On the other hand, the molecular entanglement of the PLA composites increased

in the 3D printed samples and increased when increasing the bed temperature. It was considered that molecular mobility was higher during layer deposition in the 3D printing as compared to the fast cooling in the compression molding process. Hence, the higher degree of entanglement density can be informed better layer adhesion in the 3D printing process. Nevertheless, the mechanical performance of the 3D printing might be limited by the anisotropic characteristic of the filler in the composite and the 3D printing direction [11].

The adhesion factor was calculated in the compression molded samples to inform the adhesion and the interaction between the fillers and the PLA matrix. The lower value of the adhesion factor in the PLA-CF-C indicated the higher degree of the interfacial adhesion and interfacial interaction between the CF and the PLA matrix [23,26]. The level of the adhesion factor of the particulate filler in the PLA-P-C was in the middle. The PLA-Cu-C has the high value of the adhesion factor, which the Cu particle was less interfacial adhesion with the PLA matrix as compared to the other. The effectiveness of the fillers in the composites was investigated by the effectiveness coefficient from the ratio between the  $\mathrm{E}^{\prime}$  of the glassy region (at  $40^{\circ}\mathrm{C}$ ) and the rubbery region (at  $60^{\circ}\mathrm{C}$ ). Herein, the ratio was comparison with the neat polymer of each processing condition. Higher C indicates the lower effectiveness of the filler. From the results, the high content and large particle size of the Cu particle restricted molecular mobility in the compression molded PLA-Cu-C but obtained higher effectiveness due to the molecular entanglement as reported in the rheological properties and the degree of entanglement density. While the effectiveness of the particulate filler in the PLA-P-C and the CF in the PLA-CF-C was less efficient than the Cu due to the distribution of the fillers in the PLA matrix. On the contrary, the effectiveness of the fillers was increased in the 3D printing samples and increased with increasing the bed temperature, which was attributed to higher degree of entanglement density [26,28].

Additionally, the reinforcing efficiency factor was determined to elucidate the potential of the fillers and the effect of the processing conditions on mechanical performance of the composites. According to the characteristic and properties of the filler, the CF exhibited the highest reinforcing effect in the composites from its stiffness and good distribution and interaction with the polymer matrix [23,26,28]. Moreover, the orientation of the CF along the layer deposition in the 3D printer obtain better reinforcing effect of the 3D printed PLA-CF. The good distribution of the particulate filler would support its reinforcing efficiency in the PLA-P composites. However, less adhesion and large particle size of the Cu exhibited low reinforcing efficiency in the PLA-Cu composites. It was noted that the reinforcing efficiency of the fillers in the 3D printed samples increased when increasing the bed temperature due to the increment of molecular entanglement and interaction of fillers and the PLA matrix [23,26,28].

Furthermore, the Cole-Cole analysis is obtained by plotting between the loss modulus and the storage modulus to describe homogeneity and change in the structural properties of the material system [25,26,33]. Figure 9 displays the Cole-Cole plot of the compression molded and the 3D printed PLA composites. The plot exhibited imperfect semicircle arc curves of all PLA composites, which informed the heterogeneity in the neat PLA and the composites and indicating good interfacial bonding in the composites [24]. The imperfection was improved in the 3D printing process due to the increment of the interfacial interaction and adhesion [25,33]. Devi et al. [25] and Jyoti et al. [26] reported that the shape of the Cole-Cole plot points relatively good adhesion between the matrix with glass fiber and MWCNT, respectively.

![](images/2adb795cf0f87a565622a1300c93c844de7a89156f33645b32423ca376d0a547.jpg)  
(a)

![](images/c3fdb74072416fc9849b574c1017b2b57863eeea87134505ff54c5f8d36bbf12.jpg)  
(b)

![](images/ed48c8bac6c1df363d4895624fc768f5c0ad6f4f11dad8cdad75ef7a7c597ce1.jpg)  
(c)

![](images/d2b5e25fc050510e2922d18c7ed164d0899647960e6f996c9bf794dedb9c9bce.jpg)  
(d)  
Figure 9. Cole-Cole plot of compression molded sheet and 3D printed samples: (a) PLA-N; (b) PLA-P; (c) PLA-CF; and (d) PLA-Cu.

# 3.5. Mechanical Properties

Static mechanical properties were carried out by flexural and tensile testing. Figure 10 shows typical stress-strain curves of the 3D printed samples from bed temperatures of  $45^{\circ}\mathrm{C}$  (B45) and  $60^{\circ}\mathrm{C}$  (B60). The stress increased whereas ductility of the composites decreased with increasing the bed temperature as presented in Figure 10. Flexural and tensile properties are depicted in Figure 11.

![](images/5ed481380e6f82db814a2ebf235b5e0d639ac2677e4807f32d1409b918a44b87.jpg)  
(a)

![](images/41d1f0bca291e3aa224d7b3533ab66130f3e8d6f162f4d3335afbf4fee3ecf83.jpg)  
(b)  
Figure 10. Typical stress-strain curves of 3D printed samples: (a) flexural test and (b) tensile test.

![](images/0bcf854250d60ae578a1e0dbd112ec4ee212fec54ec193efeecbf29188b117a0.jpg)  
(a)

![](images/76ab619bf727609ab5ee7d58ba7339c29bdd18eb6eef825c1aff44c20f15399d.jpg)  
(b)

![](images/e123781c2f2f70fb76b5c7a89e89fc3d9d6985ae2247565e0985263b3463b181.jpg)  
(c)

![](images/1e1775c270e4e100b72f847ffe9c3c2aed8492e0492d42e5b55c8431a01aadcf.jpg)  
(d)  
Figure 11. Flexural and tensile properties of 3D printed samples: (a) flexural modulus; (b) flexural strength; (c) tensile modulus; and (d) tensile strength.

The 3D printed at B60 obtained better stiffness and resistance of bending and tensile loading indicated by higher modulus and strength, which were due to the increment of the reinforcing efficiency factor at higher bed temperature. On the contrary, the ductility and toughness of the 3D printed promoted in the B45 samples. In the viewpoint of the incorporation of additives and layer adhesion in 3D printing, flexural and tensile modulus of the PLA-P and the PLA-CF increased by the rigidity of particulate filler and carbon fiber as presented in Figure 11a,b. In addition, the CF orientation, and its content significantly improved modulus of elasticity [20]. However, mechanical properties of the PLA-Cu were low due to less continuous of PLA matrix to withstand flexural and tensile loading from the restriction of high content of the Cu particle and the low reinforcing efficiency factor. Flexural and tensile strength of the composites were lower than the neat PLA, as shown in Figure 11c,d. It was due to the interaction between the fillers and the matrix, which limited load transferring [23] resulting in the declination of the strengths as compared to the neat PLA. It is noteworthy that the interaction and the adhesion of the fillers and the matrix yield higher mechanical properties. Therefore, the design of the 3D printing would support mechanical performance although the layer adhesion in the 3D printing might be restrict.

# 3.6. Morphology of the 3D Printed PLA Composites

Figure 12a,b display optical micrographs of the 3D printed samples at B45 and B60, respectively. Triangle voids between raster and printed layer can be seen in all 3D printed samples that indicated incomplete layer adhesion in the 3D printing process [5]. The void areas became larger in the PLA composites as compared to the neat PLA, regardless on the bed temperature. Generally, smaller void areas indicated good layer adhesion of the 3D printed samples [5,6]. Thus, fewer voids in the PLA-N implied better layer adhesion than the PLA composites 3D printings. It was considered from the effect of higher crystallization temperatures from heterogeneous additives induced faster layer solidification of molten

PLA composites and may restrict layer adhesion in the PLA composites 3D printing [22]. Nevertheless, the voids of the PLA-P were small and probably have good layer adhesion comparable to the PLA-N. It was considered that the PLA-P has high degree of entangle density and has similar flow behavior as compared to the PLA-N, while high content of the Cu particles and the flow with the rubbery phase interfered the fractured surface in the PLA-Cu-B45 and B60, which were covered existed voids. On the contrary, although the CF retarded PLA crystallization, it was the heterogeneity induced the PLA solidification resulting of large voids appeared in the PLA-CF 3D printing structure.

![](images/3b0a361545af241ed88f488a32aa35137a534ab0fcfae6ee66712b91a21af586.jpg)

![](images/b65b999fc45e314f355f1c5949baea23fca71432cf1462de539cfdda11a1631e.jpg)

![](images/888274786f7bbc00dac4b0f6b67728e1ba6f57c08ba7d1257076d78349fbd282.jpg)

![](images/a7791e6ea6766a43293212c422c67a04e4914189b1560db250ece289a2770e56.jpg)

![](images/e433d3f16cbdae66e5242d9e456a50e89a110729ad58b9c3ed9921bdffe40333.jpg)  
Figure 12. Optical micrographs of 3D printed samples: (a) at bed  $45^{\circ}\mathrm{C}$  and (b) at bed  $60^{\circ}\mathrm{C}$ .

![](images/68c880b9fbf20aa3e4e8b31eb40fa90bad3db59bcb6ba7ed2f1b42bfff00d209.jpg)  
(b)

![](images/21a068bd6fc400eeb690e67660c8e4e4ad124f099e9810a3f5a2b9c33616f536.jpg)

![](images/8cb8a5ce0638e252b38c0136e5d94d578def89e3e6aa49de871916f13a1fd56d.jpg)

Figure S3 shows densities of the PLA filaments and their compression molded and the 3D printed samples. The densities of the samples slightly changed from the filament fabricated to the compression molded sheets and the 3D printed samples. The incorporation of the additives increased the densities of the PLA composites and improved crystallinity, dynamic mechanical, flexural, and tensile properties of the polymer composites. Furthermore, the porosity inside the 3D printed samples could be implied from the density measurement [5]. The density values were unchanged in the PLA-N-B45 and the PLA-N-B60, which they were comparable in the porosity from the setting bed temperatures. The densities of the 3D printed samples slightly increased when increasing the bed temperature in the PLA-P and the PLA-CF 3D printing. It might be informed small porosity or fewer voids in the PLA-P-B60 and the PLA-CF-B60 as compared to the 3D printing at bed  $45^{\circ}\mathrm{C}$ . On the other hand, the PLA-Cu has lower porosity when printing at bed  $45^{\circ}\mathrm{C}$ . Hence, the reduction of the porosity or voids implied better layer in the 3D printings that enhanced the dimensional accuracy and the mechanical performance of the PLA composites 3D printings [5].

The effects of additives and the bed temperatures on the layer formation and the fracture behavior of the PLA composites 3D printings were observed from the tensile fractured surface. Figure 13a,b reveal the SEM images at low magnification of the 3D printed samples at B45 and B60, respectively, which the bottom of the picture closed to the printed bed. Skin-core morphology was observed in the fractured surface the PLA-N-B45 and the PLA-N-B60, in which whitening appeared at the skin of the PLA-N samples. On the other hand, the printed bed significantly affected on the fracture behavior of the PLA composites filament. The SEM images revealed ductile and brittle fracture surfaces exhibited in B45 and B60, respectively. It was considered that molecular relaxation of PLA composites at B45 was higher than B60, which indicated by intensities of the Tan  $\delta$  [23].

Then the relaxation allowed molecular movement during deformation resulting higher ductility of the PLA composites 3D printing at B45. While the composites printed at B60 were brittle, which reflected from the stiffness of the composites. From the SEM images, shrinkage slightly occurred at the bottom layers of the PLA-N-B60 and the PLA-P-B60. Therefore, it should be careful when printed on the bed temperatures higher than  $\mathrm{T_g}$  of the PLA to increase layer adhesion and maintain the dimensional stability of the PLA composites 3D printing.

![](images/a312565dcb6852ef6387a526f6a95d11cfd90ed9755845d12f2eb9934761aca5.jpg)  
Figure 13. SEM images of tensile fractured surfaces of 3D printed samples: (a) at bed  $45^{\circ}\mathrm{C}$  and (b) at bed  $60^{\circ}\mathrm{C}$ .

Figures 14 and 15 present SEM images at high magnification of the tensile fractured surfaces. The layer adhesion of the 3D printed sample was observed from the adjacent between the printed layers as shown in Figure 14. The boundary of the adjacent between printed layers can be observed from the corner of the triangle voids as indicated by the arrows, which presented the layer adhesion of the 3D printing. The neat PLA has fewer voids and no boundary of the adjacent layers, which implied superior layer adhesion of the PLA-N-B45 and the PLA-N-B60. The boundary informed the incomplete adhesion of the printed layer in the PLA composites. It was due to rapid solidification induced from the reinforced additives indicating less adhesion than the neat PLA. Although the layer adhesion in the PLA composites 3D printing was low, the molecular entanglement, the interaction of the filler and the matrix, and the reinforcing efficiency of the fillers obtained high mechanical properties that were supported their applications as compared to the neat PLA.

![](images/58de694f69fc77bee3e9959719b19f7557a1f40fa941845cb9afba0076f83130.jpg)  
PLA-N-B45

![](images/4504b20b2bced7ee62f91c030da8f331ae841fb9c2c484e14f0d42bb8fb9816f.jpg)  
PLA-P-B45

![](images/eb1e77f71dcef81730a4f298cb3a6da4241f55e0f0c2333aee366d4ba005762d.jpg)  
PLA-CF-B45

![](images/81fd65cfe8b518a4c32656cdb51ff4077169a084706acdf468e82d875b376bc7.jpg)  
PLA-Cu-B45

![](images/cc46e5e06bb17075ff74b223825052516e1baa53b3eeab2308ef5d8f5530f47d.jpg)  
PLA-N-B60

![](images/7e92fc0449b76137fef29309034ac7296431ba20b4fae479fcacb3e01e33afe9.jpg)  
PLA-P-B60  
(b)

![](images/eee793eac53f8f85e8cbf85c082983be297ad85c3f496305a21b4dc211ba6a83.jpg)  
PLA-CF-B60

![](images/3e30b312277760bd9c1dc4c5a362d0897ba5a67652960a7c64aada199779a0c0.jpg)  
PLA-Cu-B60

![](images/2607f65db95bc3f659f9a34783675ec3db65811b4d699b35f18aed6bd5d3bf5a.jpg)  
Figure 14. SEM images of tensile fractured surfaces of 3D printed samples at high magnification  $(\times 500)$ : (a) at bed  $45^{\circ}\mathrm{C}$  and (b) at bed  $60^{\circ}\mathrm{C}$ .  
PLA-N-B45

![](images/6fc96d54d5e2da64c912e7624eb4e8f2fe89c9df2e6faca3c235baaaae3005ef.jpg)

![](images/8511f4573473ae88bde7d2090c5ca3668522a81f26bf38d30026170e1143e87b.jpg)  
PLA-P-B45

![](images/e61d5c31a8a6b0b86898f9ae83839abdd2efc06f5e4d32ae544d9edb63d0aa90.jpg)  
PLA-N-B60

![](images/33d50092da2be6be88de32453cdc249ee426a219dc37bed74891035eb69920ec.jpg)  
PLA-CF-B45

![](images/4fe003d2c14bdf519fb94fa92821862cd7e5b4bbce7756bb78b850dd3772185e.jpg)  
PLA-P-B60  
PLA-CF-B60

![](images/e91323061cab1d22015fdf2994dbba7e21d3c7876f5fe7ba932e8b61c91cd855.jpg)  
PLA-Cu-B45  
Figure 15. SEM images of tensile fractured surfaces of 3D printed samples at high magnification  $(\times 1000)$ : (a) at bed  $45^{\circ}\mathrm{C}$  and (b) at bed  $60^{\circ}\mathrm{C}$ .

![](images/bce8adef984948325c9b17f5657811fc1abf658d2b9c2f56af486eed4b352ca4.jpg)  
PLA-Cu-B60  
(b)

From Figure 15, both PLA-N-B45 and PLA-N-B60 showed smooth of brittle fracture surface. Nevertheless, the elongated fibrils supported toughening and resistance to fracture in the 3D printing of the PLA-N [35]. Large deformation of the samples printed at B45 verified their ductility as depicted in Figure 15a. The elongated deformation and debonding between the additives and the PLA matrix in the PLA-P-B45 and the PLA-CF-B45 confirmed the ductility and toughening of these samples. The interfacial adhesion and the rigidity of the particulate filler and the carbon fiber improved modulus of the PLA-P-B60 and the PLA-CF-B60 even the existing of the voids. Moreover, the orientation of the carbon fiber along the 3D printing insisted the reinforcing ability in this printing direction. The SEM images of the PLA-Cu-B45 and B60 showed the rubbery dispersed phase and large copper particles that influenced on the printing ability and their layer adhesion. However, high contents of the Cu particles could support the dimensional stability and provided copper-like appearance whereas affected in low adhesion due to less PLA matrix. Thus, mechanical properties of these PLA-Cu 3D printing were poor as compared to the compression molded sheet of the PLA-Cu-C. It can be noted that the ductility of the PLA composites 3D printing improved at the lower bed temperatures owing to higher molecular relaxation [19,23]. The higher bed temperature enhanced modulus and strength of the PLA composites 3D printing. Hence, the combination of the materials' characteristics, i.e., rheological behavior and incorporation of additives and the 3D printing conditions such as printing directions, printing bed temperatures, infill, layer thickness, and so on to obtain superior mechanical properties of the 3D printing products.

# 4. Conclusions

Rheological behaviors and dynamic mechanical properties are powerful to understand the layer adhesion and the effect of additives and the bed temperatures on the properties of the PLA composites 3D printing. The Newtonian and the shear thinning flows with the moderate viscosity yielded layer stability of the molten polymer, the dimension stability, and printability of the 3D printing products. The dynamic mechanical properties informed the viscoelastic properties, the interfacial adhesion, and the interpretation of the layer adhesion in the 3D printing. The incorporation of the additives influenced on the molecular relaxation, the molecular entanglement, and the interfacial adhesion in the PLA composites. The degree of entanglement density increased when incorporated with the fillers and increasing the bed temperature. The particulate filler and the carbon fiber exhibited reinforcing efficiency and enhanced mechanical performance in these PLA composites 3D printings. However, high content of the copper particle limited the layer adhesion resulting the declination of the mechanical properties of the PLA-Cu 3D printings. The increment of the molecular relaxation in the lower bed temperature at  $45^{\circ}\mathrm{C}$  obtained high ductility and good toughness. On the contrary, the enhancing of the crystallinity, the interfacial interaction and the degree of entanglement density promoted stiffness and improved flexural and tensile properties when printed at higher bed temperature of  $60^{\circ}\mathrm{C}$ . The morphology of the PLA composites indicated incomplete and restrict of layer adhesion when incorporated with the fillers and the fiber additives. Nevertheless, the reinforcing effect, the good interfacial adhesion of the fillers with the PLA matrix and the molecular relaxation could be optimized by the incorporation of the additives and the suitable 3D printing conditions for obtaining superior mechanical performance of the PLA composites 3D printing. Nevertheless, the layer adhesion might be limited from the anisotropic characteristic of the composites and the layer-by-layer in the 3D printing. Therefore, the information in this research provides a guideline for develop new filament feed stocks, i.e., with the particulate filler, reinforcing fiber and metal powder, and processing optimization for high quality polymer composites 3D printing.

Supplementary Materials: The following supporting information can be downloaded at: https://www.mdpi.com/article/10.3390/polym14132721/s1. Figure S1. Complex viscosity as a function of angular frequency of PLA filaments. Figure S2. DSC thermograms of the enlarging cooling cycles of PLA-CF samples: (a) PLA-CF-F; (b) PLA-CF-C; (c) PLA-CF-B45; (d) PLA-CF-B60. Figure S3. Density of samples: (a) PLA-N; (b) PLA-P; (c) PLA-CF; (d) PLA-Cu.

Author Contributions: Conceptualization, H.I.; methodology, W.P., S.T. and T.K.; formal analysis, S.T. and T.K.; investigation, W.P. and S.T.; writing—original draft preparation, S.T.; writing—review and editing, A.I., T.K., S.T. and H.I.; supervision, A.I., T.K., Y.K. and H.I. All authors have read and agreed to the published version of the manuscript.

Funding: This study was funded by JSPS Grant-in-Aid for Scientific Research on Innovative Areas Grant Number JP18H05483.

Institutional Review Board Statement: Not applicable.

Data Availability Statement: The data presented in this study are available on request from the corresponding author.

Conflicts of Interest: The authors declare no conflict of interest.

# References

1. Kuncius, T.; Rimašauskas, M.; Rimašauskiené, R. Interlayer Adhesion Analysis of 3D-Printed Continuous Carbon Fibre-Reinforced Composites. Polymers 2021, 13, 1653. [CrossRef] [PubMed]  
2. Kristiawan, R.B.; Imaduddin, F.; Ariawan, D.; Ubaidillah; Arifin, Z. A review on the fused deposition modeling (FDM) 3D printing: Filament processing, materials, and printing parameters. Open Eng. 2021, 11, 639-649. [CrossRef]  
3. Duty, C.; Ajinjeru, C.; Kishore, V.; Compton, B.; Hmeidat, N.; Chen, X.; Liu, P.; Hassen, A.A.; Lindahl, J.; Kunc, V. What makes a material printable? A viscoelastic model for extrusion-based 3D printing of polymers. J. Manuf. Process. 2018, 35, 526-537. [CrossRef]  
4. Peng, F.; Vogt, B.D.; Cakmak, M. Complex flow and temperature history during melt extrusion in material extrusion additive manufacturing. Addit. Manuf. 2018, 22, 197-206. [CrossRef]  
5. Benwood, C.; Anstey, A.; Andrzejewski, J.; Misra, M.; Mohanty, A.K. Improving the Impact Strength and Heat Resistance of 3D Printed Models: Structure, Property, and Processing Correlationships during Fused Deposition Modeling (FDM) of Poly(Lactic Acid). ACS Omega 2018, 3, 4400-4411. [CrossRef]  
6. Wang, L.; Gramlich, W.M.; Gardner, D.J. Improving the impact strength of Poly(lactic acid) (PLA) in fused layer modeling (FLM). Polymer 2017, 114, 242-248. [CrossRef]  
7. Kottasamy, A.; Samykano, M.; Kadirgama, K.; Rahman, M.; Noor, M.M. Experimental investigation and prediction model for mechanical properties of copper-reinforced polylactic acid composites (Cu-PLA) using FDM-based 3D printing technique. Int. J. Adv. Manuf. Technol. 2022, 119, 5211-5232. [CrossRef]  
8. Thiam, B.G.; El Magri, A.; Vanaei, H.R.; Vaudreuil, S. 3D Printed and Conventional Membranes—A Review. Polymers 2022, 14, 1023. [CrossRef]  
9. Spoerk, M.; Gonzalez-Gutierrez, J.; Sapkota, J.; Schuschnigg, S.; Holzer, C. Effect of the printing bed temperature on the adhesion of parts produced by fused filament fabrication. Plast. Rubber Compos. 2018, 47, 17-24. [CrossRef]  
10. Nguyen, N.A.; Bowland, C.C.; Naskar, A.K. A general method to improve 3D-printability and inter-layer adhesion in lignin-based composites. Appl. Mater. Today 2018, 12, 138-152. [CrossRef]  
11. Prasong, W.; Ishigami, A.; Thumsorn, S.; Kurose, T.; Ito, H. Improvement of Interlayer Adhesion and Heat Resistance of Biodegradable Ternary Blend Composite 3D Printing. Polymers 2021, 13, 740. [CrossRef]  
12. Syrlybayev, D.; Zharylkassyn, B.; Seisekulova, A.; Akhmetov, M.; Perveen, A.; Talamona, D. Optimisation of Strength Properties of FDM Printed Parts—A Critical Review. Polymers 2021, 13, 1587. [CrossRef]  
13. Wickramasinghe, S.; Do, T.; Tran, P. FDM-Based 3D Printing of Polymer and Associated Composite: A Review on Mechanical Properties, Defects and Treatments. Polymers 2020, 12, 1529. [CrossRef]  
14. Hsueh, M.-H.; Lai, C.-J.; Wang, S.-H.; Zeng, Y.-S.; Hsieh, C.-H.; Pan, C.-Y.; Huang, W.-C. Effect of Printing Parameters on the Thermal and Mechanical Properties of 3D-Printed PLA and PETG, Using Fused Deposition Modeling. Polymers 2021, 13, 1758. [CrossRef]  
15. Basgul, C.; Thieringer, F.M.; Kurtz, S.M. Heat transfer-based non-isothermal healing model for the interfacial bonding strength of fused filament fabricated polyetheretherketone. Addit. Manuf. 2021, 46, 102097. [CrossRef]  
16. Cicala, G.; Latteri, A.; Del Curto, B.; Lo Russo, A.; Recca, G.; Fare, S. Engineering Thermoplastics for Additive Manufacturing: A Critical Perspective with Experimental Evidence to Support Functional Applications. J. Appl. Biomater. Funct. Mater. 2017, 15, 10-18. [CrossRef]  
17. Valino, A.D.; Dizon, J.R.C.; Espera, A.H.; Chen, Q.; Messman, J.; Advincula, R.C. Advances in 3D printing of thermoplastic polymer composites and nanocomposites. Prog. Polym. Sci. 2019, 98, 101162. [CrossRef]

18. Wach, R.A.; Wolszczak, P.; Adamus-Wlodarczyk, A. Enhancement of Mechanical Properties of FDM-PLA Parts via Thermal Annealing. Macromol. Mater. Eng. 2018, 303, 1800169. [CrossRef]  
19. Aw, Y.Y.; Yeoh, C.K.; Idris, M.A.; Teh, P.L.; Hamzah, K.A.; Sazali, S.A. Effect of Printing Parameters on Tensile, Dynamic Mechanical, and Thermoelectric Properties of FDM 3D Printed CABS/ZnO Composites. Materials 2018, 11, 466. [CrossRef]  
20. Ferreira, R.T.L.; Amatte, I.C.; Dutra, T.A.; Bürger, D. Experimental characterization and micrography of 3D printed PLA and PLA reinforced with short carbon fibers. Compos. Part B Eng. 2017, 124, 88-100. [CrossRef]  
21. Vanaei, H.R.; Khelladi, S.; Deligant, M.; Shirinbayan, M.; Tcharkhtchi, A. Numerical Prediction for Temperature Profile of Parts Manufactured using Fused Filament Fabrication. J. Manuf. Process. 2022, 76, 548-558. [CrossRef]  
22. Prasong, W.; Muanchan, P.; Ishigami, A.; Thumsorn, S.; Kurose, T.; Ito, H. Properties of 3D Printable Poly(lactic acid)/Poly(butylene adipate-co-terephthalate) Blends and Nano Talc Composites. J. Nanomater. 2020, 2020, 8040517. [CrossRef]  
23. Akindoyo, J.O.; Beg, M.D.H.; Ghazali, S.; Heim, H.P.; Feldmann, M.; Mariatti, M. Synergized high-load bearing bone replacement composite from poly(lactic acid) reinforced with hydroxyapatite/glass fiber hybrid filler—Mechanical and dynamic mechanical properties. Polym. Compos. 2021, 42, 57-69. [CrossRef]  
24. Mohammad, B.R.; Leman, Z.; Jawaid, M.; Ghazali, M.J.; Ishak, M.R. Dynamic mechanical analysis of treated and untreated sugar palm fibre-based phenolic composites. BioResources 2017, 12, 3448-3462. [CrossRef]  
25. Devi, L.U.; Bhagawan, S.S.; Thomas, S. Dynamic mechanical analysis of pineapple leaf/glass hybrid fiber reinforced polyester composites. Polym. Compos. 2010, 31, 956-965. [CrossRef]  
26. Jyoti, J.; Singh, B.P.; Arya, A.K.; Dhakate, S.R. Dynamic mechanical properties of multiwall carbon nanotube reinforced ABS composites and their correlation with entanglement density, adhesion, reinforcement and C factor. RSC Adv. 2016, 6, 3997-4006. [CrossRef]  
27. Kim, M.W.; Song, Y.S.; Youn, J.R. Effects of interfacial adhesion and crystallization on the thermoresistance of poly(lactic acid)/mica composites. Compos. Part A Appl. Sci. Manuf. 2010, 41, 1817-1822. [CrossRef]  
28. Madathinal Kunjappan, A.; Reghunadhan, A.; Ramachandran, A.A.; Mathew, L.; Padmanabhan, M.; Laroze, D.; Thomas, S. Discussion on degree of entanglement, chain confinement, and reinforcement efficiency factor of PTT/PE blend nanocomposite embedded with MWCNTs. Polym. Adv. Technol. 2021, 32, 2916-2928. [CrossRef]  
29. Pothan, L.A.; Oommen, Z.; Thomas, S. Dynamic mechanical analysis of banana fiber reinforced polyester composites. Compos. Sci. Technol. 2003, 63, 283-293. [CrossRef]  
30. Kaavessina, M.; Distantina, S.; Shohih, E.N.; Lomi, H.A.S.; Pratiwi, B.P.; Chafid, A. Viscoelastic Behavior and Thermal Stability of Poly(Lactic Acid) Bio-Composite Filled with Micro-Graphite. Macromol. Symp. 2020, 391, 1900140. [CrossRef]  
31. Ansari, S.; Rashid, M.A.I.; Waghmare, P.R.; Nobes, D.S. Measurement of the flow behavior index of Newtonian and shear-thinning fluids via analysis of the flow velocity characteristics in a mini-channel. SN Appl. Sci. 2020, 2, 1787. [CrossRef]  
32. Yu, W.; Wang, X.; Ferraris, E.; Zhang, J. Melt crystallization of PLA/Talc in fused filament fabrication. Mater. Des. 2019, 182, 108013. [CrossRef]  
33. Jesuarockiam, N.; Jawaid, M.; Zainudin, E.S.; Thariq Hameed Sultan, M.; Yahaya, R. Enhanced Thermal and Dynamic Mechanical Properties of Synthetic/Natural Hybrid Composites with Graphene Nanoplateletes. Polymers 2019, 11, 1085. [CrossRef] [PubMed]  
34. Dul, S.; Fambri, L.; Pegoretti, A. Filaments Production and Fused Deposition Modelling of ABS/Carbon Nanotubes Composites. Nanomaterials 2018, 8, 49. [CrossRef] [PubMed]  
35. Zeng, Q.; Feng, Y.; Wang, R.; Ma, P. Fracture behavior of highly toughened poly(lactic acid)/ethylene-co-vinyl acetate blends. e-Polymers 2018, 18, 153-162. [CrossRef]