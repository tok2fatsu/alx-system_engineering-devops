### Forecast requests faliure report
On all queries made on the platform routes, the `Forecast` platform was reportedly returning 500 Errors last week, and all of the services were unavailable. 85% of users were impacted. The failure of our master server web-01 was the primary factor.

#### Timeline
On Saturday, February 2, around 0600 (East African Time), our site reliability engineer, noticed a performance issue with the master server. For additional system examination, our on-call experts unplugged the master server web-01 and routed all requests to client server web-02. They resolved the issue by Sunday, February 3, 1500 hours (East Africa Time).

#### Cause and effect and remedy
Two Ubuntu cloud servers provide service to the `Forecast` platform. Because the client server web-02 was temporarily disconnected during a previous test and was not reconnected to the load balancer afterward, the master server web-01 couldn't handle all requests and it stopped operating due to memory outage.

The problem was resolved when the loadbalancer was restarted after the master server had been momentarily unplugged for memory cleanup, and the round-robin algorithm was set up so that both the master and client servers could handle an equal number of requests.

#### Measures against such problem in future
* Choose the best loadbalancing algorithm for your programs
* Always keep an eye on your servers to ensure they are running properly
* Have extra back-up servers to prevent your program fro completely going offline during an issue
