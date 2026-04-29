#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Prompts - 聚合物配方抽取提示词模板

此文件包含所有用于LLM抽取的提示词模板。
"""

# ============================================================================
# Prompt 模板
# ============================================================================

# 抽取配方和加工工艺的主提示词
MAJOR_POLYMER_EXTRACTION = """
interface PolymerStudy {
    isPolymerStudy: boolean;
    numFormulations: number; 
    // The number of distinct formulations extracted.
    // If the paper compares many variations (e.g., optimization of 20 different ratios),
    // extract only the most representative formulations (up to 5).
    formulations: Formulation[];
}

interface Formulation {
    id: number;

    description: string; 
    // Brief description of this specific formulation
    // (e.g., "PLA/CNT composite with 5 wt% loading").
    // IMPORTANT: This description must refer to properties measured from
    // as-printed samples using fixed/default processing parameters,
    // WITHOUT any printing or processing parameter optimization.

    // --- Material Composition ---
    polymerMatrix: {
        materialName: string; 
        // e.g., "PLA", "ABS"
        materialType: string; 
        // e.g., "NatureWorks 4043D", "Semi-crystalline"
        ratio: string; 
        // e.g., "90 wt%", "80%"
        properties: { 
            // Inherent properties of the raw polymer material (before printing or compounding)
            MFR: string | null; 
            MFI: string | null;
        }
    };

    fillers: Filler[]; 
    // Fillers used in the formulation (if any)

    additives: Additive[]; 
    // Additives such as plasticizers, stabilizers, compatibilizers (if any)

    // --- Processing ---
    processing: {
        method: string; 
        // e.g., "FDM 3D Printing", "Injection Molding", "Extrusion"
        // Printing or processing must be performed using fixed or default parameters,
        // NOT parameters obtained via systematic optimization.
        parameters: {
            processingTemperature: number | null; 
            // Nozzle temperature (printing) or barrel temperature (extrusion), numeric only (°C)
            screwSpeed: string | null; 
            // e.g., "50 rpm"
        }
    };

    // --- Resulting Properties ---
    properties: {
        mechanical: {
            tensileStrength: string | null; 
            flexuralStrength: string | null; 
            impactStrength: string | null; 
        };
        thermal: {
            heatDeflectionTemperature: string | null; 
            MFI: string | null; 
            MFR: string | null; 
        }
    };
}

interface Filler {
    name: string; 
    // e.g., "Carbon Fiber", "Graphene Oxide"
    type: string; 
    // Specific grade or form
    ratio: string; 
    // e.g., "5 wt%"
    surfaceTreatment: string | null; 
    // e.g., "Silane coupling agent"
    particleSize: string | null; 
    // e.g., "50 nm", "10 µm"
}

interface Additive {
    name: string; 
    // e.g., "Plasticizer", "Antioxidant"
    type: string;
    ratio: string;
}

/**
 * Example:
 *
 * export const polymer_data: PolymerStudy[] = [
 *   {
 *     isPolymerStudy: true,
 *     numFormulations: 1,
 *     formulations: [
 *       {
 *         id: 1,
 *         description: "PLA reinforced with 0.5 wt% functionalized Graphene Oxide, as-printed via FDM using default parameters.",
 *
 *         polymerMatrix: {
 *           materialName: "PLA",
 *           materialType: "NatureWorks 4043D",
 *           ratio: "99.5 wt%",
 *           properties: {
 *             MFR: "6 g/10 min",
 *             MFI: null
 *           }
 *         },
 *
 *         fillers: [
 *           {
 *             name: "Graphene Oxide",
 *             type: "Reduced GO",
 *             ratio: "0.5 wt%",
 *             surfaceTreatment: "Amino-functionalization",
 *             particleSize: "2–5 layers"
 *           }
 *         ],
 *
 *         additives: [],
 *
 *         processing: {
 *           method: "FDM 3D Printing",
 *           parameters: {
 *             processingTemperature: 210,
 *             screwSpeed: "null"
 *           }
 *         },
 *
 *         properties: {
 *           mechanical: {
 *             tensileStrength: "55.4 MPa",
 *             flexuralStrength: "80 MPa",
 *             impactStrength: "12 kJ/m2"
 *           },
 *           thermal: {
 *             heatDeflectionTemperature: "65 °C",
 *             MFI: null,
 *             MFR: null
 *           }
 *         }
 *       }
 *     ]
 *   }
 * ];
 */

// TODO: export formulations
export const polymer_data: PolymerStudy[] = [
];

/**
 * Notes:
 *
 * 0. **NO EXTRA KEYS (CRITICAL)**
 * - The extracted output MUST strictly conform to the interfaces defined above.
 * - ❌ DO NOT introduce, infer, rename, merge, or add ANY additional keys,
 *   nested fields, metadata, comments, or helper attributes that are NOT
 *   explicitly defined in the provided interfaces.
 * - ❌ DO NOT add fields such as:
 *   - "notes", "remarks", "source", "confidence", "assumptions"
 *   - "printingSpeed", "layerHeight", "rasterAngle"
 *   - any extra sub-objects under polymerMatrix, fillers, additives, processing, or properties
 *
 * - ✅ If a value is missing, unknown, or not reported in the paper:
 *   → Use `null` for that field (do NOT omit the field).
 *
 * - ✅ Arrays (`fillers`, `additives`) MUST be present.
 *   → Use empty arrays `[]` if none are reported.
 *
 * - ✅ All numeric fields must remain numeric (or null if unknown).
 *   → Do NOT convert numbers into strings unless the schema explicitly requires a string.
 *
 *
 * 1. **Schema Fidelity**
 * - The output MUST be valid TypeScript/JSON matching EXACTLY:
 *   - PolymerStudy
 *   - Formulation
 *   - Filler
 *   - Additive
 * - Field names, nesting depth, and data types MUST NOT be altered.
 *
 *
 * 2. **Relevance Check**
 * - Extract data ONLY if the paper involves experimental preparation,
 *   processing, or characterization of polymer formulations or composites.
 * - ❌ Ignore papers limited to:
 *   - monomer synthesis
 *   - simulations (DFT, MD, FEM)
 *   - theory without experimental material property data
 *
 *
 * 3. **Core Data Only**
 * - Do NOT extract every tested formulation.
 * - Extract ONLY:
 *   a) the most representative / baseline formulation, and/or
 *   b) the optimal formulation in terms of MATERIAL COMPOSITION
 *      (NOT processing parameter optimization).
 * - Maximum 5 formulations.
 *
 *
 * 4. **Completeness Requirement**
 * - A formulation is VALID ONLY IF it includes:
 *   - polymerMatrix.materialName
 *   - processing.method
 *   - at least ONE numerical mechanical OR thermal property
 * - If these are not available → DO NOT output the formulation.
 *
 *
 * 5. **As-Printed / As-Processed Data Only (CRITICAL)**
 * - Properties MUST be measured from samples processed using:
 *   - fixed
 *   - default
 *   - baseline
 *   - non-optimized parameters
 *
 * - ❌ DO NOT extract data obtained after:
 *   - temperature optimization
 *   - speed optimization
 *   - raster / infill / layer height optimization
 *   - multi-factor DOE studies
 *
 * - If both optimized and non-optimized results exist:
 *   → ALWAYS select the non-optimized / baseline / as-printed values.
 *
 *
 * 6. **Terminology & Units**
 * - Use explicit material names (e.g., "PLA", "ABS", "Talc").
 * - Ratios MUST include units (wt%, vol%, phr).
 * - Processing temperature MUST be a single numeric value (°C).
 *
 *
 * 7. **No Interpretation or Enrichment**
 * - ❌ DO NOT infer missing compositions, grades, or mechanisms.
 * - ❌ DO NOT summarize trends or explain results.
 * - ❌ DO NOT normalize, average, or recompute reported values.
 *
 * - ✅ Extract ONLY what is explicitly reported and fits the schema.
 */
"""

# 精炼抽取结果的提示词
MAJOR_POLYMER_EXTRACTION_REFINEMENT = """
**System Instruction: Verification and Refinement of Pre-Extracted Polymer Formulations (Step 2)**

Your task is to **refine the pre-extracted polymer formulation data** in JSON format.  
The input is a list of `PolymerStudy` objects (`PolymerStudy[]`) obtained from Step 1.  

You must carefully apply the rules below and return a **cleaned JSON output** in the exact same structure, retaining all fields from Step 1.

---

### Step 2 Rules: Filtering, Verification, and Refinement

1. **Relevance Verification**
   - If the paper is **not a true polymer experimental study**, set:
     ```json
     "isPolymerStudy": false,
     "numFormulations": 0,
     "formulations": []
     ```
   - Criteria for NOT being a polymer study:
     - No experimental polymer or composite preparation/characterization
     - Focuses only on monomer synthesis, simulations, modeling, or printer design
     - Abstract/title/conclusion does not confirm experimental polymer property data

2. **Formulation Selection**
   - Retain only **representative, baseline, or compositionally optimal formulations**.
   - Remove formulations if:
     - They are intermediate, trial, or part of a ratio sweep
     - Properties are reported only after **processing optimization**
     - Redundant with minor ratio changes
   - Maximum number of retained formulations: **5**  
   - Minimum: 0

3. **As-Printed / As-Processed Constraint**
   - Only include formulations with properties measured from **as-printed, as-extruded, or as-molded samples**.
   - Remove formulations measured after **systematic parameter optimization** (temperature, speed, layer height, infill, raster, etc.)
   - If both optimized and non-optimized data exist, select **non-optimized** data

4. **Composition Accuracy**
   - **Polymer matrix** must be explicitly named; do not infer grades/crystallinity unless stated
   - **Fillers** must be explicitly mentioned; do not infer from vague terms like “reinforced”
   - **Additives** include only explicitly stated plasticizers, stabilizers, compatibilizers, antioxidants
   - Leave `fillers` or `additives` as empty arrays if none are reported

5. **Property Validation**
   - At least one numerical value is required in:
     - Mechanical: `tensileStrength`, `flexuralStrength`, `impactStrength`
     - OR Thermal: `heatDeflectionTemperature`, `MFI`, `MFR`
   - Remove formulations with only qualitative or figure-based descriptions

6. **Consistency**
   - `numFormulations` = number of retained formulations
   - `id` fields must be sequential starting from 1
   - Retain **all original fields** from Step 1 (`description`, `polymerMatrix`, `fillers`, `additives`, `processing`, `properties`)
   - Descriptions must be **short, technical, and composition-focused**, without optimization or speculative claims

---

### Output Format

Return the refined PolymerStudy data as JSON (`PolymerStudy[]`), preserving all fields:

```json
[
  {
    "isPolymerStudy": true | false,
    "numFormulations": 0-5,
    "formulations": [
      {
        "id": 1,
        "description": "string",
        "polymerMatrix": {
          "materialName": "string",
          "materialType": "string",
          "ratio": "string",
          "properties": {
            "MFR": "string | null",
            "MFI": "string | null"
          }
        },
        "fillers": [
          {
            "name": "string",
            "type": "string",
            "ratio": "string",
            "surfaceTreatment": "string | null",
            "particleSize": "string | null"
          }
        ],
        "additives": [
          {
            "name": "string",
            "type": "string",
            "ratio": "string"
          }
        ],
        "processing": {
          "method": "string",
          "parameters": {
            "processingTemperature": number | null,
            "screwSpeed": "string | null"
          }
        },
        "properties": {
          "mechanical": {
            "tensileStrength": "string | null",
            "flexuralStrength": "string | null",
            "impactStrength": "string | null"
          },
          "thermal": {
            "heatDeflectionTemperature": "string | null",
            "MFI": "string | null",
            "MFR": "string | null"
          }
        }
      }
    ]
  }
]
"""

# 抽取工艺参数的提示词
PRINTING_OPTIMIZATION_EXTRACTION = """
/**
 * Step 3: Printing / Processing Optimization Extraction
 * 
 * Goal: For each pre-extracted polymer formulation (from Step 1/2), 
 * extract representative printing or processing optimization experiments 
 * (parameter variations like temperature, speed, infill, etc.) and their resulting mechanical properties,
 * and attach them to the original formulation data.
 */

interface PolymerStudyWithOptimization {
    // Keep all original fields from Step 1/2
    isPolymerStudy: boolean;
    numFormulations: number;
    formulations: FormulationWithOptimization[];
}

interface FormulationWithOptimization {
    // Original formulation info
    id: number;
    description: string;
    polymerMatrix: {
        materialName: string;
        materialType: string;
        ratio: string;
        properties: { MFR: string | null; MFI: string | null };
    };
    fillers: Filler[];
    additives: Additive[];
    processing: {//Don’t add any other key–value pairs beyond this.
        method: string;
        parameters: { processingTemperature: number | null; screwSpeed: string | null };
    };
    properties: {
        mechanical: {//Don’t add any other key–value pairs beyond this.
            tensileStrength: string | null;
            flexuralStrength: string | null;
            impactStrength: string | null;
        };
        thermal: { heatDeflectionTemperature: string | null; MFI: string | null; MFR: string | null };
    };

    // New field: printing/processing optimization data
    optimizationData?: PrintingOptimizationDataset[];
}

interface PrintingOptimizationDataset {
    studyDescription: string; // short description, e.g., "Effect of nozzle temperature on tensile strength"
    constantParameters: {
        printerType: string | null;
        nozzleDiameter: string | null;
        layerHeight: string | null;
        infillPattern: string | null;
        [otherConstantParam: string]: string;
    };
    dataPoints: OptimizationRun[];
}

interface OptimizationRun {
    conditions: {//Don’t add any other key–value pairs beyond this.
        printingTemperature: string | null;
        printingSpeed: string | null;
        bedTemperature: string | null;
        infillDensity: string | null;
        [otherVariableParam: string]: string;
    };
    properties: {//Don’t add any other key–value pairs beyond this.
        tensileStrength: string | null;
        flexuralStrength: string | null;
        impactStrength: string | null;
    };
}
* 0. **NO EXTRA KEYS (ABSOLUTE RULE)**
 * - The extracted output MUST strictly conform to the interfaces defined above:
 *   - PolymerStudyWithOptimization
 *   - FormulationWithOptimization
 *   - PrintingOptimizationDataset
 *   - OptimizationRun
 *
 * - ❌ DO NOT introduce, infer, rename, merge, or add ANY additional keys,
 *   nested objects, metadata fields, comments, or helper attributes
 *   that are NOT explicitly defined in these interfaces.
 *
 * - ❌ Specifically forbidden (non-exhaustive):
 *   - Any keys like "notes", "remarks", "source", "figure", "table", "confidence"
 *   - Any processing or printing parameters NOT represented as:
 *     - constantParameters
 *     - conditions
 *   - Any extra nesting under properties, conditions, or parameters
 *
 *
 * 1. **Dynamic Keys Are Still Constrained**
 * - Keys using index signatures:
 *   - [otherConstantParam: string]: string
 *   - [otherVariableParam: string]: string
 *   are ONLY allowed inside:
 *   - constantParameters
 *   - conditions
 *
 * - ❌ Such dynamic keys MUST NOT appear anywhere else.
 * - ❌ Do NOT create new objects to store them.
 *
 *
 * 2. **Missing or Unreported Values**
 * - If a REQUIRED field is mentioned in the interface but not reported:
 *   → set its value to `"null"` or `"null"` (as a string, per interface usage).
 *
 * - ❌ Do NOT omit required fields.
 * - ❌ Do NOT guess or infer values.
 *
 *
 * 3. **Optional Field Handling**
 * - `optimizationData` is optional:
 *   - If NO optimization experiments exist → omit the field OR use an empty array `[]`.
 *   - If optimization exists → include ONLY valid `PrintingOptimizationDataset` objects.
 *
 *
 * 4. **Schema Fidelity**
 * - Field names, nesting depth, and data types MUST match the interfaces EXACTLY.
 * - ❌ Do NOT:
 *   - change arrays into objects
 *   - collapse multiple studies into one
 *   - split one study across multiple schemas
 *
 *
 * 5. **Optimization Data Scope**
 * - ONLY include experiments where printing or processing parameters were
 *   systematically varied.
 * - ❌ Do NOT include:
 *   - baseline / default printing results (already captured in Step 1/2)
 *   - single-point trials with no comparison
 *
 *
 * 6. **Data Point Selection**
 * - Include AT MOST 5 representative `OptimizationRun`s per
 *   `PrintingOptimizationDataset`.
 * - Choose typical or central values.
 * - ❌ Avoid extreme, failure, or outlier cases unless explicitly described
 *   as representative in the paper.
 *
 *
 * 7. **No Interpretation or Enrichment**
 * - ❌ Do NOT explain trends, mechanisms, or conclusions.
 * - ❌ Do NOT normalize, average, interpolate, or recompute values.
 * - ❌ Do NOT merge data across different figures, tables, or studies.
 *
 * - ✅ Extract ONLY what is explicitly reported and fits EXACTLY into the schema.
 */

/**
 * Instructions:
 * 1. For each formulation, extract **representative optimization experiments** from the paper.
 * 2. Only include experiments where printing/processing parameters were systematically varied.
 * 3. Preserve all original formulation information; attach optimization data under `optimizationData`.
 * 4. For each data point, map conditions to the resulting mechanical properties exactly.
 * 5. If a property is not tested, set as "null" or "null".
 * 6. Only include up to 5 representative runs per optimization study; choose typical/central values, not extreme outliers.
 * 7. Retain units as reported (MPa, °C, mm/s, %, etc.).
 * 8. Include constant parameters like printer type, nozzle diameter, layer height, infill pattern, bed temp if not varied.
 * 9. If no optimization study exists for a formulation, omit `optimizationData` or set as an empty array.
 */

/**
 * Example output:
 */
export const polymer_data_with_optimization: PolymerStudyWithOptimization[] = [
    {
        formulations: [
            {
                id: 1,
                description: "PLA reinforced with 0.5 wt% functionalized Graphene Oxide, as-printed via FDM using default parameters.",
                polymerMatrix: {
                    materialName: "PLA",
                    materialType: "NatureWorks 4043D",
                    ratio: "99.5 wt%",
                    properties: { MFR: "6 g/10 min", MFI: null }
                },
                fillers: [
                    {
                        name: "Graphene Oxide",
                        type: "Reduced GO",
                        ratio: "0.5 wt%",
                        surfaceTreatment: "Amino-functionalization",
                        particleSize: "2–5 layers"
                    }
                ],
                additives: [],
                processing: {
                    method: "FDM 3D Printing",
                    parameters: { processingTemperature: 210°C, screwSpeed: "null" }
                },
                properties: {
                    mechanical: { tensileStrength: "55.4 MPa", flexuralStrength: "80 MPa", impactStrength: "12 kJ/m2" },
                    thermal: { heatDeflectionTemperature: "65 °C", MFI: null, MFR: null }
                },
                optimizationData: [
                    {
                        studyDescription: "Effect of nozzle temperature on tensile strength",
                        constantParameters: {
                            printerType: "Prusa i3 MK3",
                            nozzleDiameter: "0.4 mm",
                            layerHeight: "0.2 mm",
                            infillPattern: "Rectilinear"
                        },
                        dataPoints: [
                            {
                                conditions: { printingTemperature: "190 °C", printingSpeed: "40 mm/s", bedTemperature: "60 °C", infillDensity: "100%" },
                                properties: { tensileStrength: "50.1 MPa", flexuralStrength: "78 MPa", impactStrength: "11.5 kJ/m2" }
                            },
                            {
                                conditions: { printingTemperature: "200 °C", printingSpeed: "40 mm/s", bedTemperature: "60 °C", infillDensity: "100%" },
                                properties: { tensileStrength: "55.4 MPa", flexuralStrength: "80 MPa", impactStrength: "12 kJ/m2" }
                            },
                            {
                                conditions: { printingTemperature: "210 °C", printingSpeed: "40 mm/s", bedTemperature: "60 °C", infillDensity: "100%" },
                                properties: { tensileStrength: "53.2 MPa", flexuralStrength: "79 MPa", impactStrength: "12.2 kJ/m2" }
                            }
                        ]
                    }
                ]
            }
        ]
    }
];

// TODO: export polymer_data_with_optimization
export const polymer_data_with_optimization: PolymerStudyWithOptimization[] = [
];
"""

# 优化精炼提示词
PRINTING_OPTIMIZATION_EXTRACTION_REFINED = "I will provide a literature text and a JSON data table describing a single 3D printing formulation, including material composition, processing parameters, and resulting properties. The information table may be incomplete or contain uncertainties. Based on the formulation, processing conditions, and results described in the text, you need to verify whether the existing entries in the JSON are correct. If any values are missing, empty, or marked as unknown, you should complete the formulation details, printing parameters, or material properties as accurately as possible using the information from the text."
