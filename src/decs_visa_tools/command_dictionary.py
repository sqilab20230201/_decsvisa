"""
Module that contains the 'command dictionaries" for various
oi:DECS system types
"""

#   A system dictionary that maps 'short' commands to the
#   WAMP uri that provides the functionality

#   Whilst the exact 'short' name is flexible, there is a convention that needs to be followed.
#   This is because the type/format of the uri args and/or the returned WAMP 'record types' may
#   depend on which uri is being called and so some method of grouping the commands to allow
#   parsing is required.

#   GET or SET - it is assumed that all commands either set something on the system, or request
#   information from it, therefore all commands must start with either:
#
#   get_    For a command that is requesting information, or
#   set_    For a command that is setting a value on the system
#
#   With one or two exceptions - the PUBLISH command writes to a topic rather than calling
#   an rRPC, so this is a special case.
#
#   And a version of a *IDN? command is implemented to allow and oi:DECS driver to be implemented
#   in a straightforward way in QCoDeS.

ProteoxMX_cmd_uri = {
    "get_MC_T"          : "oi.decs.temperature_control.DRI_MIX_CL.DRI_MIX_S.temperature",
    "set_MC_T"          : "oi.decs.temperature_control.DRI_MIX_CL.setpoint",
    "get_MC_H"          : "oi.decs.temperature_control.DRI_MIX_CL.DRI_MIX_H.power",
    "set_MC_H"          : "oi.decs.temperature_control.DRI_MIX_CL.DRI_MIX_H.power",
    "set_MC_H_OFF"      : "oi.decs.temperature_control.DRI_MIX_CL.DRI_MIX_H.power",
    "get_STILL_T"       : "oi.decs.temperature_control.DRI_STL_S.temperature",
    "get_STILL_H"       : "oi.decs.temperature_control.DRI_STL_H.power",
    "set_STILL_H"       : "oi.decs.temperature_control.DRI_STL_H.power",
    'set_STILL_H_OFF'   : "oi.decs.temperature_control.DRI_STL_H.power",
    "get_CP_T"          : "oi.decs.temperature_control.DRI_CLD_S.temperature",
    "get_SRB_T"         : "oi.decs.temperature_control.SRB_GGS_CL.SRB_GGS_S.temperature",
    "get_DR2_T"         : "oi.decs.temperature_control.DRI_PT2_S.temperature",
    "get_PT2_T1"        : "oi.decs.temperature_control.PTR1_PT2_S.temperature",
    "get_DR1_T"         : "oi.decs.temperature_control.DRI_PT1_S.temperature",
    "get_PT1_T1"        : "oi.decs.temperature_control.PTR1_PT1_S.temperature",
    "get_OVC_P"         : "oi.decs.proteox.OVC_PG_01.pressure",
    "get_P1_P"          : "oi.decs.proteox.3CL_PG_01.pressure",
    "get_P2_P"          : "oi.decs.proteox.3CL_PG_02.pressure",
    "get_P3_P"          : "oi.decs.proteox.3CL_PG_03.pressure",
    "get_P4_P"          : "oi.decs.proteox.3CL_PG_04.pressure",
    "get_P5_P"          : "oi.decs.proteox.3CL_PG_05.pressure",
    "get_P6_P"          : "oi.decs.proteox.3CL_PG_06.pressure",
    "get_MAG_T"         : "oi.decs.magnetic_field_control.MAG_MSP_S.temperature",
    "get_MAG_VEC"        : "oi.decs.magnetic_field_control.VRM_01.magnetic_field_vector",
    "get_MAG_STATE"      : "oi.decs.magnetic_field_control.VRM_01.state",
    "get_SWZ_STATE"      : "oi.decs.magnetic_field_control.VRM_01.SWZ.state",
    "set_MAG_TARGET"     : "oi.decs.magnetic_field_control.VRM_01.set_field_target",
    "set_MAG_STATE"      : "oi.decs.magnetic_field_control.VRM_01.set_state",
    "set_MAG_X_STATE"    : "oi.decs.magnetic_field_control.VRM_01.MAG_X.set_state",
    "set_MAG_Y_STATE"    : "oi.decs.magnetic_field_control.VRM_01.MAG_Y.set_state",
    "set_MAG_Z_STATE"    : "oi.decs.magnetic_field_control.VRM_01.MAG_Z.set_state",
    "get_MAG_CURR_VEC"   : "oi.decs.magnetic_field_control.VRM_01.current_vector",
    "set_CURR_TARGET"    : "oi.decs.magnetic_field_control.VRM_01.set_output_current_target",
    "PUBLISH"           : "oi.decs.proteox.eventlog",
    "get_a_WAMP_error"  : "oi.decs.THIS_WONT_WORK", # used for testing only
    "set_a_WAMP_error"  : "oi.decs.THIS_WONT_WORK"
}

Teslatron_cmd_uri = {
    "get_PROBE_T"        : "oi.decs.temperature_control.PROBE_CL.PROBE_S.temperature",
    "set_PROBE_T"        : "oi.decs.temperature_control.PROBE_CL.setpoint",
    "get_PROBE_TARGET_T" : "oi.decs.temperature_control.PROBE_CL.setpoint",
    "get_PROBE_H"        : "oi.decs.temperature_control.PROBE_CL.PROBE_H.power",
    "set_PROBE_H"        : "oi.decs.temperature_control.PROBE_CL.PROBE_H.set_power",
    "set_PROBE_H_OFF"    : "oi.decs.temperature_control.PROBE_CL.PROBE_H.set_power",
    "get_PROBE_PID_P"    : "oi.decs.temperature_control.PROBE_CL.p_term",
    "get_VTI_T"          : "oi.decs.temperature_control.VTI_CL.VTI_S.temperature",
    "set_VTI_T"          : "oi.decs.temperature_control.VTI_CL.setpoint",
    "get_VTI_TARGET_T"   : "oi.decs.temperature_control.VTI_CL.setpoint",
    "get_VTI_H"          : "oi.decs.temperature_control.VTI_CL.VTI_H.power",
    "set_VTI_H"          : "oi.decs.temperature_control.VTI_CL.VTI_H.set_power",
    "set_VTI_H_OFF"      : "oi.decs.temperature_control.VTI_CL.VTI_H.set_power",
    "get_PT2_T"          : "oi.decs.temperature_control.PT2_S.temperature",
    "get_PT1_T"          : "oi.decs.temperature_control.PT1_S.temperature",
    "get_PRES"           : "oi.decs.pressure_control.NV_CL.VTI_PG.pressure",
    "get_TARGET_PRES"    : "oi.decs.pressure_control.NV_CL.pressure_setpoint",
    "set_PRES"           : "oi.decs.pressure_control.NV_CL.set_pressure_setpoint",
    "get_NEEDLE_PERC"    : "oi.decs.pressure_control.NV_CL.pressure_setpoint",
    "set_NEEDLE_PERC"    : "oi.decs.pressure_control.NV_CL.set_valve_open_percentage",
    "get_MAG_T"          : "oi.decs.magnetic_field_control.MAG_MSP_S.temperature",
    "get_MAG_VEC"        : "oi.decs.magnetic_field_control.VRM_01.magnetic_field_vector",
    "get_MAG_STATE"      : "oi.decs.magnetic_field_control.VRM_01.state",
    "get_SWZ_STATE"      : "oi.decs.magnetic_field_control.VRM_01.SWZ.state",
    "set_MAG_TARGET"     : "oi.decs.magnetic_field_control.VRM_01.set_field_target",
    "set_MAG_STATE"      : "oi.decs.magnetic_field_control.VRM_01.set_state",
    "set_MAG_X_STATE"    : "oi.decs.magnetic_field_control.VRM_01.MAG_X.set_state",
    "set_MAG_Y_STATE"    : "oi.decs.magnetic_field_control.VRM_01.MAG_Y.set_state",
    "set_MAG_Z_STATE"    : "oi.decs.magnetic_field_control.VRM_01.MAG_Z.set_state",
    "get_MAG_CURR_VEC"   : "oi.decs.magnetic_field_control.VRM_01.current_vector",
    "set_CURR_TARGET"    : "oi.decs.magnetic_field_control.VRM_01.set_output_current_target",
    "get_SAMPLE_ANG"     : "oi.decs.sample_rotator.TP_SR_01.position",
    "set_SAMPLE_ANG"     : "oi.decs.sample_rotator.TP_SR_01.set_target_position",
    "PUBLISH"            : "oi.decs.proteox.eventlog",
    "get_a_WAMP_error"   : "oi.decs.THIS_WONT_WORK", # used for testing only
    "set_a_WAMP_error"   : "oi.decs.THIS_WONT_WORK"
}

APS_demo_2024_cmd_uri = {
    "get_T"              : "oi.decs.temperature_control.DRI_PT2_S.temperature",
    "get_SAMPLE_ANG"     : "oi.decs.sample_rotator.TP_SR_01.position",
    "set_SAMPLE_ANG"     : "oi.decs.sample_rotator.TP_SR_01.set_target_position",
    "get_PULSE_WIDTH"    : "oi.decs.sample_rotator.TP_SR_01.pulse_width",
    "set_PULSE_WIDTH"    : "oi.decs.sample_rotator.TP_SR_01.set_pulse_width",
    "get_MIN_ANGLE"      : "oi.decs.sample_rotator.TP_SR_01.min_angle",
    "get_MAX_ANGLE"      : "oi.decs.sample_rotator.TP_SR_01.max_angle",
    "PUBLISH"            : "oi.decs.proteox.eventlog",
    "get_a_WAMP_error"   : "oi.decs.THIS_WONT_WORK", # used for testing only
    "set_a_WAMP_error"   : "oi.decs.THIS_WONT_WORK"
}


someOtherSystemType = {
    # Implement other/further cmd_dict(s) as required
    "short_cmd"         : "wamp.uri"
}
