/-
Copyright (c) 2026 Joris Roos. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Claude
-/
module

public import Isoperim.DIR.«1_Introduction».Definitions
public import Isoperim.DIR.«2_Envelope_Functions».Definitions
public import Isoperim.DIR.«3_Variants_Bobkov_Inequality».«3_0_Variants_Bobkov_Inequality_aux»
public import Isoperim.DIR.«3_Variants_Bobkov_Inequality».«3_0_Variants_Bobkov_Inequality»
public import Isoperim.DIR.«4_Computer_Assisted_Proofs».«4_1_Dyadic_Partitioning_aux»
public import Isoperim.DIR.«4_Computer_Assisted_Proofs».«4_1_Dyadic_Partitioning»
public import Isoperim.DIR.«4_Computer_Assisted_Proofs».«4_2_Interval_Arithmetic_aux»
public import Isoperim.DIR.«4_Computer_Assisted_Proofs».«4_2_Interval_Arithmetic»
public import Isoperim.DIR.«4_Computer_Assisted_Proofs».«4_3_Source_Code_aux»
public import Isoperim.DIR.«4_Computer_Assisted_Proofs».«4_3_Source_Code»
public import Isoperim.DIR.«5_Auxiliary_Estimates».«5_3_Properties_L_Q_aux»
public import Isoperim.DIR.«5_Auxiliary_Estimates».«5_3_Properties_L_Q»
public import Isoperim.DIR.«5_Auxiliary_Estimates».«5_2_Two_Point_Inequalities_aux»
public import Isoperim.DIR.«5_Auxiliary_Estimates».«5_2_Two_Point_Inequalities»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_cert»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_tab_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_tab_1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_tab_2»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_tab_3»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_2»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_3»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_4»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_5»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_6»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_7»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_8»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_9»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_10»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_11»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_12»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_13»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_14»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_box_15»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ2_main»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1_tabJ_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1_tabJ_1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1_tabJ_2»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1_tabJ_3»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1_tabJ_4»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1_tabD_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1_tabD_1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1_tabD_2»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1_tabD_3»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1a_tabP_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1a_tabP_1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1a_tabP_2»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1a_tabP_3»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1a_tabP_4»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1a_box_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1a_box_1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1a_box_2»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1a_box_3»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1a_box_4»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1a_box_5»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1a_main»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1b_tabP_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1b_tabP_1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1b_tabP_2»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1b_box_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1b_box_1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1b_box_2»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1b_box_3»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_gJ1b_main»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J_aux_cont»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_1_Case_J»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_2_Case_Q»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_b0_tab_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_b0_tab_1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_b0_tab_2»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_b0_box_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_b0_box_1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_b0_box_2»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_b0_box_3»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_b0_box_4»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_b0_main»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_h_tab_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_h_tab_1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_h_tab_2»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_h_box_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_h_box_1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_h_box_2»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_h_box_3»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_h_box_4»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g1_h_main»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g2»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ_aux_g2_main»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_3_Case_LJQ»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_4_Case_LJ_aux»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_4_Case_LJ»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_5_Case_QJQ_aux»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_5_Case_QJQ_aux_cert»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_5_Case_QJQ_aux_cert_tab_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_5_Case_QJQ_aux_cert_b1_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_5_Case_QJQ_aux_cert_b1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_5_Case_QJQ_aux_cert_h_0»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_5_Case_QJQ_aux_cert_h_1»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_5_Case_QJQ_aux_cert_h»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_5_Case_QJQ»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_6_Case_QJ_aux»
public import Isoperim.DIR.«6_Proof_Two_Point_Inequality».«6_6_Case_QJ»
public import Isoperim.DIR.«2_Envelope_Functions».«2_0_Envelope_Functions»
public import Isoperim.DIR.«5_Auxiliary_Estimates».«5_4_Lower_Bounds_Gaussian_Isoperimetric_Profile»
public import Isoperim.DIR.«2_Envelope_Functions».«2_2_Proofs_Theorems_1_1_1_5_1_7»
public import Isoperim.DIR.«5_Auxiliary_Estimates».«5_1_Small_Exponents_Large_Exponents»
public import Isoperim.DIR.«1_Introduction».Thm_1_1
public import Isoperim.DIR.«1_Introduction».Thm_1_5
public import Isoperim.DIR.«1_Introduction».Thm_1_6
public import Isoperim.DIR.«1_Introduction».Thm_1_7
public import Isoperim.DIR.«7_Proof_Poincare_Inequality».«7_0_Proof_Poincare_Inequality»
public import Isoperim.DIR.«1_Introduction».Thm_1_10
public import Isoperim.DIRX.«1_Introduction».Definitions
public import Isoperim.DIRX.«2_Preliminaries».Definitions
public import Isoperim.DIRX.«2_Preliminaries».«2_2_Properties_J»
public import Isoperim.DIRX.«3_Proof_Two_Point_Inequality».«3_1_Case_J»
public import Isoperim.DIRX.«3_Proof_Two_Point_Inequality».«3_2_Case_Q»
public import Isoperim.DIRX.«2_Preliminaries».«2_3_Properties_L_Q»
public import Isoperim.DIRX.«3_Proof_Two_Point_Inequality».«3_3_Case_LJQ»
public import Isoperim.DIRX.«3_Proof_Two_Point_Inequality».«3_4_Case_LJ»
public import Isoperim.DIRX.«3_Proof_Two_Point_Inequality».«3_5_Case_QJQ»
public import Isoperim.DIRX.«3_Proof_Two_Point_Inequality».«3_6_Case_QJ»
public import Isoperim.DIRX.«2_Preliminaries».«2_1_Reduction_Two_Point_Inequality»
public import Isoperim.DIRX.«1_Introduction».Thm_1_1
public import Isoperim.DIRX.«1_Introduction».Thm_1_2
public import Isoperim.DIRX.«4_Proof_Poincare_Inequality».«4_0_Proof_Poincare_Inequality»
public import Isoperim.DIRX.«1_Introduction».Thm_1_3

/-!
# Isoperim

This file was automatically generated by Claude.

Root module of the `Isoperim` library: imports the statement scaffolds of
[DIR] (arXiv:2407.12674v2, namespace `Auto.DIR`) and [DIRX] (arXiv:2602.20462v1, namespace
`Auto.DIRX`), in the order of the papers.
-/
