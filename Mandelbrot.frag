#version 330 core
out vec4 FragColor;

uniform float zoom;
uniform vec2 offset;

int mandelbrot(vec2 c) {
    vec2 z = vec2(0.0);
    int max_iter = 1000;
    for (int i = 0; i < max_iter; ++i) {
        float x = (z.x * z.x - z.y * z.y) + c.x;
        float y = (2.0 * z.x * z.y) + c.y;
        z = vec2(x, y);
        if (dot(z, z) > 4.0) return i;
    }
    return max_iter;
}

void main() {
    vec2 c = (gl_FragCoord.xy / 1080.0 - vec2(0.5)) * 3.0 * zoom + offset;
    int m = mandelbrot(c);
    float color = float(m) / 100.0;
    FragColor = vec4(vec3(color), 1.0);
}
