set ns [new Simulator]
set trace_file [open distance_vector.tr w]
set nam_file [open distance_vector.nam w]
$ns trace-all $trace_file
$ns namtrace-all $nam_file

proc finish {} {
    global ns trace_file nam_file
    $ns flush-trace
    close $trace_file
    close $nam_file
    puts "Wrote distance_vector.tr and distance_vector.nam"
    exit 0
}

for {set i 0} {$i < 5} {incr i} {
    set n($i) [$ns node]
}
$ns duplex-link $n(0) $n(1) 1Mb 10ms DropTail
$ns duplex-link $n(1) $n(2) 1Mb 10ms DropTail
$ns duplex-link $n(0) $n(3) 1Mb 15ms DropTail
$ns duplex-link $n(3) $n(2) 1Mb 15ms DropTail
$ns duplex-link $n(2) $n(4) 1Mb 10ms DropTail
$ns rtproto DV

set udp [new Agent/UDP]
set sink [new Agent/Null]
$ns attach-agent $n(0) $udp
$ns attach-agent $n(4) $sink
$ns connect $udp $sink
set traffic [new Application/Traffic/CBR]
$traffic set packetSize_ 500
$traffic set interval_ 0.02
$traffic attach-agent $udp

$ns at 0.5 "$traffic start"
$ns rtmodel-at 2.0 down $n(1) $n(2)
$ns rtmodel-at 4.0 up $n(1) $n(2)
$ns at 5.0 "$traffic stop"
$ns at 5.2 "finish"
$ns run
