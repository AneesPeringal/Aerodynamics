r1 = [-1.9866e+04,4.1141e+03,1.03130e+04];
r2 = [-1.3244e+04,5.0952e+03,9.0799e+03];
r3 = [-1.8185e+04,-2.4487e+04,5.146e+03];
v1 = [-1.9283,-4.6569,-0.8754];
v2 = [-3.72701,-4.8142,-0.5383];
v3 = [1.9060,-2.3528,-2.2838];
plot_orbit(r1,v1)
plot_orbit(r2,v2)
plot_orbit(r3,v3)
function plot_orbit(RO,VO)
R =6378;
%Solve set of differential equations in the ECI frame
time=[0:10:10000000];

XO2=[RO VO];

tol=1e-6;
options=odeset('RelTol',tol);

%ode45 matlab integrator - type "help ode45"
[t,X2]=ode45(@two_body,time,XO2,options);
fig = figure();
plot3(X2(:,1),X2(:,2),X2(:,3));
hold on;
grid on;
plot3(0,0,0,'or'); hold on; grid on; %center of the Earth
%Earth Plot
rectangle('Position',[-R -R 2*R 2*R],'Curvature',[1,1],'EdgeColor','r'); hold on; grid on;
xlabel('x(km)');
ylabel('y(km)');
zlabel('z(km)');
end

function xdot=two_body(t,X)

Mu=3.986004e5;

r=norm(X(1:3));

xdot=[X(4);
X(5);
X(6);
-Mu*X(1)/r^3 ;
-Mu*X(2)/r^3 ;
-Mu*X(3)/r^3];
end
