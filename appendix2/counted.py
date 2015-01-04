First word               Value     Meaning
MAGIC                    1337      Identifies the file as being .COUNTED format.
TEMPORARY_FILE           101       Marks the file up as being temporary
STOP_METADATA            102       Marks the end of the metadata header
SCAN_TYPE                103       101: Dip/fringe, 102: Static sample, 103: Scripted scan
SCAN_NSTEPS              201       Number of steps per loop
SCAN_NLOOPS              202       Number of repeated loops in total scan
SCAN_INTEGRATION_TIME    203       Integration time per measurement, ms
SCAN_CLOSE_SHUTTER       204       Whether or not the laser shutter was closed at the end of the scan
SCAN_DONT_MOVE           205       If true, motors were disabled during the scan
SCAN_MOTOR_CONTROLLER    206       Index number of the motor controller used. 
SCAN_START_POSITION      207       Motor controller position at start of scan, mm / degrees
SCAN_STOP_POSITION       208       Motor controller position at end of scan, mm / degrees
SCAN_LABEL_NBYTES        250       Length in bytes of a text label, which follows this record

Measurement data
MOTOR_CONTROLLER_UPDATE  301       Records motor controller index and position.
SCAN_LOOP                302       Loop index
SCAN_STEP                303       Step index
INTEGRATION_STEP         304       Integration step number
STOP_INTEGRATING         305       Written when integration has finished
START_COUNT_RATES        401       Start a list of measured countrates
COUNT_RATE               402       Detection pattern as a binary string, and number of events
STOP_COUNT_RATES         403       End the list of countrates
START_PAUSE              404       Experimentalist paused the measurement
STOP_PAUSE               405       Experimentalist resumed the measurement
