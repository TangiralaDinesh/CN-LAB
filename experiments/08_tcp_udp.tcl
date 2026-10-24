set ns [new Simulator]
set trace_file [open tcp_udp.tr w]
set nam_file [open tcp_udp.nam w]
$ns trace-all $trace_file
$ns namtrace-all $nam_file

proc finish {} {
    global ns trace_file nam_file
    $ns flush-trace
    close $trace_file
    close $nam_file
    puts "Wrote tcp_udp.tr and tcp_udp.nam"
    exit 0
}

set tcp_source [$ns node]
set udp_source [$ns node]
set router [$ns node]
set destination [$ns node]

$ns duplex-link $tcp_source $router 2Mb 10ms DropTail
$ns duplex-link $udp_source $router 2Mb 10ms DropTail
$ns duplex-link $router $destination 1Mb 20ms DropTail
$ns queue-limit $router $destination 10

set tcp [new Agent/TCP]
set tcp_sink [new Agent/TCPSink]
$ns attach-agent $tcp_source $tcp
$ns attach-agent $destination $tcp_sink
$ns connect $tcp $tcp_sink
$tcp set fid_ 1
set ftp [new Application/FTP]
$ftp attach-agent $tcp

set udp [new Agent/UDP]
set udp_sink [new Agent/Null]
$ns attach-agent $udp_source $udp
$ns attach-agent $destination $udp_sink
$ns connect $udp $udp_sink
$udp set fid_ 2
set cbr [new Application/Traffic/CBR]
$cbr set packetSize_ 1000
$cbr set rate_ 1Mb
$cbr set random_ false
$cbr attach-agent $udp

$ns at 0.1 "$cbr start"
$ns at 1.0 "$ftp start"
$ns at 4.0 "$ftp stop"
$ns at 4.5 "$cbr stop"
$ns at 5.0 "finish"
$ns run
