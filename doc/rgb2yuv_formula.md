# The formulas of RGB to YUV conversion

The original formulas is
Y = 0.299R + 0.587G + 0.114B
U = 0.492(B - Y)
V = 0.877(R - Y)
which are equal to
Y = ( 0.299R) + ( 0.587G) + ( 0.114B)
U = (-0.147R) + (-0.289G) + ( 0.436B)
V = ( 0.615R) + (-0.515G) + (-0.100B)

---

The formulas above is one kind of formulas used in TV. Our case use a kind of 'PC' formulas, according to '基于MATLAB和FPGA的图像处理教程' by CrazyBing (韩彬)
Y = 0.299R + 0.587G + 0.114B
U = 0.568(B - Y) + 128
V = 0.713(R - Y) + 128 
which are equal to
Y = ( 0.299R) + ( 0.587G) + ( 0.114B)
U = (-0.172R) + (-0.339G) + ( 0.511B) + 128
V = ( 0.511R) + (-0.428G) + (-0.083B) + 128
The above formulas is from OV7725 datasheet
