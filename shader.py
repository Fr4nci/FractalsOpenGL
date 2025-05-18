import OpenGL.GL as gl

class Shader:
    def __init__(self, vertex_path, fragment_path):
        with open(vertex_path) as f:
            vertex_src = f.read()
        with open(fragment_path) as f:
            fragment_src = f.read()

        self.program = gl.glCreateProgram()
        vertex_shader = self._compile_shader(vertex_src, gl.GL_VERTEX_SHADER)
        fragment_shader = self._compile_shader(fragment_src, gl.GL_FRAGMENT_SHADER)

        gl.glAttachShader(self.program, vertex_shader)
        gl.glAttachShader(self.program, fragment_shader)
        gl.glLinkProgram(self.program)

        if not gl.glGetProgramiv(self.program, gl.GL_LINK_STATUS):
            raise RuntimeError(gl.glGetProgramInfoLog(self.program).decode())

        gl.glDeleteShader(vertex_shader)
        gl.glDeleteShader(fragment_shader)

    def _compile_shader(self, src, shader_type):
        shader = gl.glCreateShader(shader_type)
        gl.glShaderSource(shader, src)
        gl.glCompileShader(shader)

        if not gl.glGetShaderiv(shader, gl.GL_COMPILE_STATUS):
            raise RuntimeError(gl.glGetShaderInfoLog(shader).decode())
        return shader

    def use(self):
        gl.glUseProgram(self.program)

    def set_uniform(self, name, value):
        location = gl.glGetUniformLocation(self.program, name)
        if isinstance(value, (float, int)):
            gl.glUniform1f(location, float(value))
        elif isinstance(value, (list, tuple)) and len(value) == 2:
            gl.glUniform2f(location, value[0], value[1])
