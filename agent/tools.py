from fluent.mock_controller import MockFluent 


# Create our fake Fluent session
fluent = MockFluent()


def get_fluent_status():
    """Get the current status of the Fluent simulation."""

    return fluent.get_fluent_status()


def get_mesh_info():
    """Get information about the current computational mesh."""

    return fluent.get_mesh_info()


def get_boundary_info():
    """Get the available boundary zones."""

    return fluent.get_boundary_info()


def set_velocity_inlet(
    boundary_name: str,
    velocity: float
):
    """Set the velocity magnitude of a velocity inlet."""

    return fluent.set_velocity_inlet(
        boundary_name,
        velocity
    )


def set_pressure_outlet(
    boundary_name: str,
    pressure: float = 0.0
):
    """Set the gauge pressure of a pressure outlet."""

    return fluent.set_pressure_outlet(
        boundary_name,
        pressure
    )


def set_material(
    material_name: str,
    cell_zone_name: str
):
    """Assign a material to a fluid cell zone."""

    return fluent.set_material(
        material_name,
        cell_zone_name
    )


def initialize_solution():
    """Initialize the CFD solution."""

    return fluent.initialize_solution()


def run_iterations(iterations: int):
    """Run the specified number of solver iterations."""

    return fluent.run_iterations(iterations)


def get_residuals():
    """Get the current solver residuals."""

    return fluent.get_residuals()


# All tools that Gemini is allowed to use
TOOLS = [
    get_fluent_status,
    get_mesh_info,
    get_boundary_info,
    set_velocity_inlet,
    set_pressure_outlet,
    set_material,
    initialize_solution,
    run_iterations,
    get_residuals
 
]
