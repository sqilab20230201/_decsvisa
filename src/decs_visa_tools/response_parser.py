"""
Module that implements the WAMP response parsing
"""
from enum import IntEnum

from autobahn.wamp.types import CallResult

from .base_logger import logger


class OIRecordType(IntEnum):
    """ Utility class to allow the various OIDataRecord
    types to be accessed as enum values"""
    TEMPERATURE = 0
    PRESSURE = 10
    MASS_FLOW = 20
    VOLUME_FLOW = 30
    MAG_FIELD = 40
    CURRENT = 50
    VOLTAGE = 60
    POWER = 70
    FREQUENCY = 80
    RESISTANCE = 90
    SW_STATE = 1020
    HTR_POWER = 1040
    CONTROL_LOOP = 1050
    PRES_CONTROL_LOOP = 1070
    ANGULAR_POS = 1090
    MAG_FIELD_VEC = 1400
    PSU_CURRENT_VEC = 1410
    SPEED = 10010

# | Value | Data Record Type                                                  |
# |------:|:------------------------------------------------------------------|
# |     0 | [OiTemperatureRecord](#temperature-record)                        |
# |    10 | [OiPressureRecord](#pressure-record)                              |
# |    20 | [OiMassFlowRecord](#mass-flow-record)                             |
# |    30 | [OiVolumetricFlowRecord](#volumetric-flow-record)                 |
# |    40 | [OiMagneticFieldRecord](#magnetic-field-record)                   |
# |    50 | [OiCurrentRecord](#current-record)                                |
# |    60 | [OiVoltageRecord](#voltage-record)                                |
# |    70 | [OiPowerRecord](#power-record)                                    |
# |    80 | [OiFrequencyRecord](#frequency-record)                            |
# |    90 | [OiResistanceRecord](#resistance-record)                          |
# |   100 | [OiQuadratureRecord](#quadrature-record)                          |
# |  1000 | [OiValveStateRecord](#valve-state-record)                         |
# |  1010 | [OiPumpSpeedRecord](#pump-speed-record)                           |
# |  1020 | [OiSwitchStateRecord](#switch-state-record)                       |
# |  1030 | [OiOnOffStateRecord](#on-off-state-record)                        |
# |  1040 | [OiHeaterPowerRecord](#heater-power-record)                       |
# |  1050 | [OiControlLoopRecord](#control-loop-record)                       |
# |  1060 | [OiUpsStateRecord](#ups-state-record)                             |
# |  1070 | [OiPressureControlLoopRecord](#pressure-control-loop-record)      |
# |  1090 | [OiAngularPositionRecord](#angular-position-record)               |
# |  1100 | [OiDigitalInputStateRecord](#digital-input-state-record)          |
# |  1110 | [OiDigitalOutputStateRecord](#digital-output-state-record)        |
# |  1120 | [OiPressureSwitchStateRecord](#pressure-switch-state-record)      |
# |  1200 | [OiCountRecord](#count-record)                                    |
# |  1201 | [OiPercentageRecord](#percentage-record)                          |
# |  1202 | [OiRatioRecord](#ratio-record)                                    |
# |  1400 | [OiMagnetFieldVectorRecord](#magnet-field-vector-record)          |
# |  1410 | [OiMagnetCurrentVectorRecord](#magnet-current-vector-record)      |
# |  1420 | [OiMagnetPsuGroupStateRecord](#magnet-psu-group-state-record)     |
# |  1430 | [OiExcitationRecord](#excitation-record)                          |
# |  1440 | [OiLakeshoreConfigurationRecord](#lakeshore-configuration-record) |
# |  1450 | [OiHeliumReadingModeRecord](#helium-reading-mode-record)       |
# |  5000 | [OiProteoxStateRecord](#proteox-record)                           |
# |  6000 | [OiLiquidReservoirStateRecord](#liquidreservoir-record)           |
# | 10000 | [OiUnknownIntegerRecord](#unknown-integer-record)                 |
# | 10010 | [OiUnknownDoubleRecord](#unknown-double-record)                   |
# | 10020 | [OiUnknownStringRecord](#unknown-string-record)                   |
# | 10030 | [OiUnknownBooleanRecord](#unknown-boolean-record)                 |


def decs_response_parser(resp: CallResult) -> str:
    """
    Based on the response 'message type' (oiDataRecord) determine which
    part(s) of the WAMP data record to return
    """
    n_args = len(resp.results)
    if n_args == 1:
        # Not all responses are consistent in the API - this will catch
        # and retrun 'flat' responses until the API fix is implemented
        logger.debug("Parsing flat response: %s", str(resp.results))
        return str(resp.results[0])
    if n_args == 2:
        # Not all responses are consistent in the API - this will catch
        # and retrun magnet state responses until the API fix is implemented
        logger.debug("Parsing flat response: %s", str(resp.results))
        return str(resp.results[0])
    if n_args == 9:
        # Not all responses are consistent in the API - this will catch
        # and retrun magnet state responses until the API fix is implemented
        print(resp.results)
        logger.debug("Parsing flat response: %s", str(resp.results))
        return float(resp.results[0]), float(resp.results[1]), float(resp.results[2])
    
    # For longer data records, the first data element
    # in the response results should be the record type
    data_record_type = int(resp.results[0])

    logger.debug("Parsing response: %s", str(resp.results))

    # In principle each of these records could be handled separately, however
    # many records have similar 'shape' so these are currently grouped together.
    # Any future oi:DECS API change may require these to be split out should the
    # response results be altered.

    # match the record type (requires python >= 3.10)
    try:
        if data_record_type == OIRecordType.TEMPERATURE or \
                data_record_type == OIRecordType.PRESSURE or \
                data_record_type == OIRecordType.MASS_FLOW or \
                data_record_type == OIRecordType.VOLUME_FLOW or \
                data_record_type == OIRecordType.MAG_FIELD or \
                data_record_type == OIRecordType.CURRENT or \
                data_record_type == OIRecordType.VOLTAGE or \
                data_record_type == OIRecordType.POWER or \
                data_record_type == OIRecordType.FREQUENCY or \
                data_record_type == OIRecordType.RESISTANCE or \
                data_record_type == OIRecordType.SPEED:
            assert n_args == 6, "Length of data record inconsistent with record type"
            return str(resp.results[4])
        elif data_record_type == OIRecordType.CONTROL_LOOP or\
                data_record_type == OIRecordType.ANGULAR_POS or\
                data_record_type == OIRecordType.SW_STATE:
            assert n_args == 7, "Length of data record inconsistent with record type"
            return str(resp.results[4])
        elif data_record_type == OIRecordType.HTR_POWER:
            assert n_args == 8, "Length of data record inconsistent with record type"
            return str(resp.results[4])
        elif data_record_type == OIRecordType.MAG_FIELD_VEC or \
                data_record_type == OIRecordType.PSU_CURRENT_VEC:
            assert n_args == 8, "Length of data record inconsistent with record type"
            return float(resp.results[4]), float(resp.results[5]), float(resp.results[6])
        elif data_record_type == OIRecordType.PRES_CONTROL_LOOP:
            assert n_args == 11, "Length of data record inconsistent with record type"
            return str(resp.results[5])
        else:
            # Shouldn't have gotten to here
            raise NotImplementedError(f"Unable to match data record type: {str(data_record_type)}")
    except (AssertionError, NotImplementedError) as e:
        logger.info("Error parsing response: %s", e)
        return str(e)
