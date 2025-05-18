import numpy as np
import glfw
import OpenGL.GL as gl
from shader import Shader

class MandelbrotRenderer:
    def __init__(self, width, height):
        self.shader = Shader("shader.vert", "BurningShip.frag")
        self.width = width
        self.height = height
        self.zoom = 1.0
        self.offset = [0.0, 0.0]

        self.vertices = np.array([
            -1.0, -1.0,
             1.0, -1.0,
             1.0,  1.0,
            -1.0,  1.0
        ], dtype=np.float32)

        self.indices = np.array([
            0, 1, 2,
            2, 3, 0
        ], dtype=np.uint32)

        self._setup_buffers()

    def _setup_buffers(self):
        self.VAO = gl.glGenVertexArrays(1)
        self.VBO = gl.glGenBuffers(1)
        self.EBO = gl.glGenBuffers(1)

        gl.glBindVertexArray(self.VAO)

        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.VBO)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, gl.GL_STATIC_DRAW)

        gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, self.EBO)
        gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, gl.GL_STATIC_DRAW)

        gl.glVertexAttribPointer(0, 2, gl.GL_FLOAT, gl.GL_FALSE, 2 * 4, gl.ctypes.c_void_p(0))
        gl.glEnableVertexAttribArray(0)

        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
        gl.glBindVertexArray(0)

    def draw(self):
        self.shader.use()
        self.shader.set_uniform("zoom", self.zoom)
        self.shader.set_uniform("offset", self.offset)
        gl.glBindVertexArray(self.VAO)
        gl.glDrawElements(gl.GL_TRIANGLES, 6, gl.GL_UNSIGNED_INT, None)
        gl.glBindVertexArray(0)

    def handle_input(self, window):
        if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
            self.offset[1] += 0.005 * self.zoom
        if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
            self.offset[1] -= 0.005 * self.zoom
        if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
            self.offset[0] -= 0.005 * self.zoom
        if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
            self.offset[0] += 0.005 * self.zoom
        if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
            self.zoom *= 0.985
        if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
            self.zoom /= 0.985

    def cleanup(self):
        gl.glDeleteVertexArrays(1, [self.VAO])
        gl.glDeleteBuffers(1, [self.VBO])
        gl.glDeleteBuffers(1, [self.EBO])
