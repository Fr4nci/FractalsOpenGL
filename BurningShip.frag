#version 330 core
out vec4 FragColor;

uniform float zoom;
uniform vec2 offset;

int burningShip(vec2 c) {
    vec2 z = vec2(0.0);
    int max_iter = 500;
    for (int i = 0; i < max_iter; ++i) {
        z = vec2(abs(z.x), abs(z.y));
        float x = z.x * z.x - z.y * z.y + c.x;
        float y = 2.0 * z.x * z.y + c.y;
        z = vec2(x, y);
        if (dot(z, z) > 4.0) return i;
    }
    return max_iter;
}

void main() {
    // Risoluzione hardcoded: 1080x1080
    vec2 uv = gl_FragCoord.xy / 1080.0;

    // Inverti l'asse y per evitare la specchiatura
    uv.y = 1.0 - uv.y;

    // Mappatura nello spazio complesso centrato sul Burning Ship
    vec2 c = (uv - vec2(0.5)) * 3.0 * zoom + offset;

    int m = burningShip(c);
    float color = float(m) / 500.0;
    FragColor = vec4(vec3(color), 1.0);
}
