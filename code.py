GlowScript 3.0 VPython

scene = canvas(background = color.black) 

T = text(text='ECHO', align='center', color=color.green) 
T.height = (3e4)*T.height
T.length = (3e4)*T.length
T.depth = (3e4)*T.depth

K = text(text='2021', align='center', color=color.yellow)

G = 6.7e-11

Sun = sphere(pos = vec(0,0,0), m = 2e30, radius = 10 * 7e8,
                color = color.yellow, make_trail = True) #makes visual rtail
                #trail_type = 'points', interval = 80, retain = 30) 
Sun.v = vec(0,0,0) 
Sun.p = Sun.m * Sun.v

Earth = sphere(pos = vec(1.5e11, 0, 0), m = 1e24, radius = 6 * 6.4e8,
                texture= textures.earth, make_trail= True) 
                #trail_type = 'points', interval = 80, retain = 50) 

Earth.v = vec(0,2.8e4,0) 
Earth.p = Earth.m * Earth.v 

gr_p = graph(title = ' Earth p(t) diagram ' , xtitle = 't' , ytitle = 'p(t)') 

p_plot_E_x = gcurve(graph = gr_p, color = color.red) 
p_plot_E_y = gcurve(graph = gr_p, color = color.blue) 
p_plot_E_z = gcurve(graph = gr_p, color = color.green) 
 

gr_p_S = graph(title = ' Sun p(t) diagram ' , xtitle = 't' , ytitle = 'p(t)')

p_plot_S_x = gcurve(graph = gr_p_S, color = color.red) 
p_plot_S_y = gcurve(graph = gr_p_S, color = color.blue) 
p_plot_S_z = gcurve(graph = gr_p_S, color = color.green) 

gr_pt = graph(title = ' Total p(t) diagram ' , xtitle = 't' , ytitle = 'p(t)')

p_plot_pt_x = gcurve(graph = gr_pt, color = color.red) 
p_plot_pt_y = gcurve(graph = gr_pt, color = color.blue) 
p_plot_pt_z = gcurve(graph = gr_pt, color = color.green) 

myrate = 1000

R = Earth.pos - Sun.pos

t= 0 
dt = 60 * 60

while t < 5 * 365 * 24 * 60 * 60 : # 5 years 

        rate(myrate) 
        R = Earth.pos - Sun.pos
        Rhat = R/mag(R) 
        
        Fmag = G * Sun.m * Earth.m / mag(R)**2
        F_onEarth = Fmag * (-Rhat) 
        Earth.p = Earth.p + F_onEarth * dt
        Earth.pos = Earth.pos + (Earth.p/Earth.m) * dt
        
        F_onSun = -F_onEarth
        Sun.p = Sun.p + F_onSun * dt
        Sun.pos = Sun.pos + (Sun.p/Sun.m) * dt
       
        
        p_plot_E_x.plot(pos = (t,Earth.v.x)) 
        p_plot_E_y.plot(pos = (t,Earth.v.y)) 
        p_plot_E_z.plot(pos = (t,Earth.v.z)) 
        
        p_plot_S_x.plot(pos = (t,Sun.v.x))
        p_plot_S_y.plot(pos = (t,Sun.v.y)) 
        p_plot_S_z.plot(pos = (t,Sun.v.z)) 
        
        p_plot_pt_x.plot(pos = (t, Earth.p.x))
        p_plot_pt_y.plot(pos = (t, Earth.p.y))
        p_plot_pt_z.plot(pos = (t, Earth.p.z))
        
        t = t + dt
