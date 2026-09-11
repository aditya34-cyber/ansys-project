
from dotenv import load_dotenv
import os
import ansys.fluent.core as pyfluent 
load_dotenv()
api_key= os.getenv("MY_GEMINI_KEY")


from google import genai #type: ignore
api = genai.Client(api_key=api_key)
solver = pyfluent.launch_fluent(
    mode = "solver"
    ui_mode= "gui"
)



# ---------------------------------------------------------
# 1. Get Fluent status
# ---------------------------------------------------------

def get_fluent_status(solver):
    """Return basic information about the current Fluent session."""

    return {
        "connected": solver is not None,
        "status": "Fluent session is active"
    }


# ---------------------------------------------------------
# 2. Get mesh information
# ---------------------------------------------------------

def get_mesh_info(solver):
    """Return basic mesh information."""

    mesh = solver.settings.mesh

    return {
        "mesh_available": mesh is not None,
        "message": "Mesh information retrieved from Fluent."
    }


# ---------------------------------------------------------
# 3. Get boundary information
# ---------------------------------------------------------

def get_boundary_info(solver):
    """Return the available boundary zones."""

    boundaries = solver.settings.setup.boundary_conditions

    return {
        "available_boundary_types": [
            "velocity_inlet",
            "pressure_inlet",
            "pressure_outlet",
            "mass_flow_inlet",
            "wall",
            "symmetry"
        ],
        "message": "Boundary-condition interface is available."
    }


# ---------------------------------------------------------
# 4. Set velocity inlet
# ---------------------------------------------------------

def set_velocity_inlet(
    solver,
    boundary_name: str,
    velocity: float
):
    """Set velocity magnitude for a velocity inlet."""

    if velocity < 0:
        raise ValueError("Velocity cannot be negative.")

    inlet = solver.settings.setup.boundary_conditions.velocity_inlet[
        boundary_name
    ]

    inlet.momentum.velocity_magnitude = velocity

    return {
        "success": True,
        "boundary": boundary_name,
        "velocity": velocity,
        "unit": "m/s"
    }


# ---------------------------------------------------------
# 5. Set pressure outlet
# ---------------------------------------------------------

def set_pressure_outlet(
    solver,
    boundary_name: str,
    pressure: float = 0.0
):
    """Set gauge pressure for a pressure outlet."""

    outlet = solver.settings.setup.boundary_conditions.pressure_outlet[
        boundary_name
    ]

    outlet.momentum.gauge_pressure = pressure

    return {
        "success": True,
        "boundary": boundary_name,
        "pressure": pressure,
        "unit": "Pa"
    }


# ---------------------------------------------------------
# 6. Set material
# ---------------------------------------------------------

def set_material(
    solver,
    material_name: str,
    cell_zone_name: str
):
    """Assign a material to a fluid cell zone."""

    cell_zone = solver.settings.setup.cell_zone_conditions[
        cell_zone_name
    ]

    cell_zone.material.material_name = material_name

    return {
        "success": True,
        "material": material_name,
        "cell_zone": cell_zone_name
    }


# ---------------------------------------------------------
# 7. Initialize solution
# ---------------------------------------------------------

def initialize_solution(solver):
    """Initialize the Fluent solution."""

    solver.settings.solution.initialization.hybrid_initialize()

    return {
        "success": True,
        "message": "Solution initialized using hybrid initialization."
    }


# ---------------------------------------------------------
# 8. Run iterations
# ---------------------------------------------------------

def run_iterations(
    solver,
    iterations: int
):
    """Run a specified number of solver iterations."""

    if iterations <= 0:
        raise ValueError("Number of iterations must be greater than zero.")

    solver.settings.solution.run_calculation.iterate(
        number_of_iterations=iterations
    )

    return {
        "success": True,
        "iterations": iterations,
        "message": f"Fluent completed {iterations} iterations."
    }


# ---------------------------------------------------------
# 9. Get residuals
# ---------------------------------------------------------

def get_residuals(solver):
    """Return the current residual history."""

    residuals = solver.settings.solution.monitor.residual

    return {
        "success": True,
        "residuals": residuals
    }
prompt = input("What do you want me to simulate? ")

response = api.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\nGemini:")
print(response.text)