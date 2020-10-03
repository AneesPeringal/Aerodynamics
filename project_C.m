%%planet parameters
planet


%%initial conditions
r1 = [-19866.1384654013,4114.06053776140,10313.0993841333];
v1 = [-1.92830013810959,-4.65685220824058,-0.875380380014480];

stateinitial = [r1(1),r1(2),r1(3),v1(1),v1(2),v1(3)];


%%time period
a = 45000;
P = 2*pi/sqrt(mu)*a^(3/2);
tspan = [0 P];
option = odeset('RelTol',1e-6)
[tout, stateout] = ode45(@odefun,tspan,stateinitial,option); 

%%plotting
fig = figure();
xout = stateout(:,1);
yout = stateout(:,2);
zout = stateout(:,3);

plot3(xout,yout,zout,'-')
grid on
hold on
function dstatedt = odefun(t,state)
planet
r = state(1:3);
rnorm = norm(r);
rhat = r/rnorm;
vel = state(4:6);


acc = -(mu/rnorm^3)*r;

dstatedt = [vel;acc];
end
