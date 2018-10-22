import pytest
import os



class TestImpedanceBackground:

    OPEN = False
    SHORT = True

    # response codes
    GEN_SUCCESS=0xFF
    RESP_BGND_IMPEDANCE_CHECK_FAILED=0x81

    # active errors
    ACTERR_SIGNAL_OPEN_NOSTOP = 61
    ACTERR_CH_IMPEDANCE_FAILURE_PROGRAMS_DISABLED = 34
    ACTERR_CH_IMPEDANCE_FAILURE_SHORT_PROGRAMS_DISABLED = 36



    # typedef union IMPCHK
    # {
    #    struct
    #    {
    # 	    uint8_t enabled        :1;  ///< Bit 0 the background impedance check is enabled (value 1) or disabled (value 0).
    # 	    uint8_t openDetection  :1;  ///< Bit 1  turns on (1) or off (0) open detection.
    # 	    uint8_t closeDetection :1;  ///< Bit 2  turns on (1) or off (0) close detection.
    # 	    uint8_t StopOnOpen     :1;  ///< Bit 3  if 1, and on demand impedance measurement test reports open, the STIM is stopped.
    #       uint8_t reserved       :4;
    #    } ;
    #    uint8_t bgiFlags;      ///< Background Impedance control settings.
    # } IMPCHK;
    
    @pytest.mark.parametrize(
        "bgi_flags, short,     high_risk,   exp_return_code,     exp_active_err", [
         # enabled=0,openDetection=0,closeDetection=0,StopOnOpen=0
        (0x00,      OPEN,      False,      GEN_SUCCESS, 0),
        (0x00,      OPEN,      True,       GEN_SUCCESS, 0),
        (0x00,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x00,      SHORT,     True,       GEN_SUCCESS, 0),
         # enabled=1,openDetection=0,closeDetection=0,StopOnOpen=0
        (0x01,      OPEN,      False,      GEN_SUCCESS, 0),
        (0x01,      OPEN,      True,       GEN_SUCCESS, 0),
        (0x01,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x01,      SHORT,     True,       GEN_SUCCESS, 0),
         # enabled=0,openDetection=1,closeDetection=0,StopOnOpen=0
        (0x02,      OPEN,      False,      GEN_SUCCESS, 0),
        (0x02,      OPEN,      True,       GEN_SUCCESS, 0),
        (0x02,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x02,      SHORT,     True,       GEN_SUCCESS, 0),
         # enabled=1,openDetection=1,closeDetection=0,StopOnOpen=0
        (0x03,      OPEN,      False,      GEN_SUCCESS, ACTERR_SIGNAL_OPEN_NOSTOP),
        (0x03,      OPEN,      True,       GEN_SUCCESS, ACTERR_SIGNAL_OPEN_NOSTOP),
        (0x03,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x03,      SHORT,     True,       GEN_SUCCESS, 0),
         # enabled=0,openDetection=0,closeDetection=1,StopOnOpen=0
        (0x04,      OPEN,      False,      GEN_SUCCESS, 0),
        (0x04,      OPEN,      True,       GEN_SUCCESS, 0),
        (0x04,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x04,      SHORT,     True,       GEN_SUCCESS, 0),
         # enabled=1,openDetection=0,closeDetection=1,StopOnOpen=0
        (0x05,      OPEN,      False,      GEN_SUCCESS, 0),
        (0x05,      OPEN,      True,       GEN_SUCCESS, 0),
        (0x05,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x05,      SHORT,     True,       RESP_BGND_IMPEDANCE_CHECK_FAILED, ACTERR_CH_IMPEDANCE_FAILURE_SHORT_PROGRAMS_DISABLED),
         # enabled=0,openDetection=1,closeDetection=1,StopOnOpen=0
        (0x06,      OPEN,      False,      GEN_SUCCESS, 0),
        (0x06,      OPEN,      True,       GEN_SUCCESS, 0),
        (0x06,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x06,      SHORT,     True,       GEN_SUCCESS, 0),
         # enabled=1,openDetection=1,closeDetection=1,StopOnOpen=0
        (0x07,      OPEN,      False,      GEN_SUCCESS, ACTERR_SIGNAL_OPEN_NOSTOP),
        (0x07,      OPEN,      True,       GEN_SUCCESS, ACTERR_SIGNAL_OPEN_NOSTOP),
        (0x07,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x07,      SHORT,     True,       RESP_BGND_IMPEDANCE_CHECK_FAILED, ACTERR_CH_IMPEDANCE_FAILURE_SHORT_PROGRAMS_DISABLED),
         # enabled=0,openDetection=0,closeDetection=0,StopOnOpen=1
        (0x08,      OPEN,      False,      GEN_SUCCESS, 0),
        (0x08,      OPEN,      True,       GEN_SUCCESS, 0),
        (0x08,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x08,      SHORT,     True,       GEN_SUCCESS, 0),
         # enabled=1,openDetection=0,closeDetection=0,StopOnOpen=1
        (0x09,      OPEN,      False,      GEN_SUCCESS, 0),
        (0x09,      OPEN,      True,       GEN_SUCCESS, 0),
        (0x09,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x09,      SHORT,     True,       GEN_SUCCESS, 0),
         # enabled=0,openDetection=0,closeDetection=0,StopOnOpen=1
        (0x0A,      OPEN,      False,      GEN_SUCCESS, 0),
        (0x0A,      OPEN,      True,       GEN_SUCCESS, 0),
        (0x0A,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x0A,      SHORT,     True,       GEN_SUCCESS, 0),
         # enabled=1,openDetection=0,closeDetection=0,StopOnOpen=1
        (0x0B,      OPEN,      False,      RESP_BGND_IMPEDANCE_CHECK_FAILED, ACTERR_CH_IMPEDANCE_FAILURE_PROGRAMS_DISABLED),
        (0x0B,      OPEN,      True,       RESP_BGND_IMPEDANCE_CHECK_FAILED, ACTERR_CH_IMPEDANCE_FAILURE_PROGRAMS_DISABLED),
        (0x0B,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x0B,      SHORT,     True,       GEN_SUCCESS, 0),
         # enabled=1,openDetection=0,closeDetection=0,StopOnOpen=1
        (0x0C,      OPEN,      False,      GEN_SUCCESS, 0),
        (0x0C,      OPEN,      True,       GEN_SUCCESS, 0),
        (0x0C,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x0C,      SHORT,     True,       GEN_SUCCESS, 0),
         # enabled=1,openDetection=0,closeDetection=0,StopOnOpen=1
        (0x0D,      OPEN,      False,      GEN_SUCCESS, 0),
        (0x0D,      OPEN,      True,       GEN_SUCCESS, 0),
        (0x0D,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x0D,      SHORT,     True,       RESP_BGND_IMPEDANCE_CHECK_FAILED, ACTERR_CH_IMPEDANCE_FAILURE_SHORT_PROGRAMS_DISABLED),
         # enabled=0,openDetection=1,closeDetection=1,StopOnOpen=1
        (0x0E,      OPEN,      False,      GEN_SUCCESS, 0),
        (0x0E,      OPEN,      True,       GEN_SUCCESS, 0),
        (0x0E,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x0E,      SHORT,     True,       GEN_SUCCESS, 0),
         # enabled=1,openDetection=1,closeDetection=1,StopOnOpen=1
        (0x0F,      OPEN,      False,      RESP_BGND_IMPEDANCE_CHECK_FAILED, ACTERR_CH_IMPEDANCE_FAILURE_PROGRAMS_DISABLED),
        (0x0F,      OPEN,      True,       RESP_BGND_IMPEDANCE_CHECK_FAILED, ACTERR_CH_IMPEDANCE_FAILURE_PROGRAMS_DISABLED),
        (0x0F,      SHORT,     False,      GEN_SUCCESS, 0),
        (0x0F,      SHORT,     True,       RESP_BGND_IMPEDANCE_CHECK_FAILED, ACTERR_CH_IMPEDANCE_FAILURE_SHORT_PROGRAMS_DISABLED),
    ])

    def test_expected_values_start(self, bgi_flags, short, high_risk, exp_return_code, exp_active_err):

        my_return_code = self.GEN_SUCCESS
        my_active_err = 0

        global_enabled       = bgi_flags & 0x01
        open_chan_detection  = (bgi_flags & 0x02) >> 1
        short_chan_detection = (bgi_flags & 0x04) >> 2
        disable_prog_on_open = (bgi_flags & 0x08) >> 3

        #print("bgi_flags: 0x%02x global_enabled: %s open_chan_detection: %s disable_prog_on_open: %s short_chan_detection: %s" % (bgi_flags,global_enabled,open_chan_detection,disable_prog_on_open,short_chan_detection))

        if global_enabled:
            if short:
                if short_chan_detection:
                    if high_risk:
                        my_return_code = self.RESP_BGND_IMPEDANCE_CHECK_FAILED
                        my_active_err = self.ACTERR_CH_IMPEDANCE_FAILURE_SHORT_PROGRAMS_DISABLED
            else: #open
                if open_chan_detection :
                    if disable_prog_on_open:
                        my_return_code = self.RESP_BGND_IMPEDANCE_CHECK_FAILED
                        my_active_err = self.ACTERR_CH_IMPEDANCE_FAILURE_PROGRAMS_DISABLED
                    else:
                        my_active_err = self.ACTERR_SIGNAL_OPEN_NOSTOP
            

        #if my_return_code == exp_return_code and my_active_err == exp_active_err:
        #    return

        #print("bgi_flags: 0x%02x, short: %s, high_risk: %s, my_return_code: %d, exp_return_code: %d my_active_err: %d, exp_active_err: %d" % \
        #       (bgi_flags,short,high_risk,my_return_code,exp_return_code,my_active_err,exp_active_err))
        assert my_return_code == exp_return_code
        assert my_active_err == exp_active_err


