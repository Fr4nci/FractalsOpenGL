import glfw
import OpenGL.GL as gl
import numpy as np
from shader import Shader
from mandelbrot_render import MandelbrotRenderer

WIDTH, HEIGHT = 1920, 1080

def framebuffer_size_callback(window, width, height):
    gl.glViewport(0, 0, width, height)

def main():
    if not glfw.init():
        raise Exception("GLFW initialization failed")

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(WIDTH, HEIGHT, "Mandelbrot", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Failed to create window")

    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)

    renderer = MandelbrotRenderer(WIDTH, HEIGHT)

    while not glfw.window_should_close(window):
        gl.glClearColor(0.1, 0.0, 0.1, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        renderer.handle_input(window)
        renderer.draw()

        glfw.swap_buffers(window)
        glfw.poll_events()

    renderer.cleanup()
    glfw.terminate()

if __name__ == "__main__":
    main()
