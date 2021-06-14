import os
import compas

from compas.robots import LocalPackageMeshLoader
from compas.robots import RobotModel
from compas_fab.robots import RobotSemantics

# Set high precision to import meshes defined in meters
compas.PRECISION = '12f'
# models_path = os.path.join(os.path.dirname(__file__), 'models')
models_path = r'C:\Users\gcasas\eth\Workshops\COMPAS-II-FS2021\docker\irb910sc-planner'

# Prepare loader
loader = LocalPackageMeshLoader(models_path, 'abb_irb910sc_support')

# Create robot model from URDF
model = RobotModel.from_urdf_file(loader.load_urdf(r'C:\Users\gcasas\eth\Workshops\COMPAS-II-FS2021\docker\irb910sc-planner\abb_irb910sc_support\urdf\irb910sc_3_065.urdf'))

semantics = RobotSemantics.from_srdf_file(r'C:\Users\gcasas\eth\Workshops\COMPAS-II-FS2021\docker\irb910sc-planner\abb_irb910sc_3_065_moveit_config\config\irb910.srdf', model)
# Load geometry
model.load_geometry(loader)
from compas_fab.robots import Robot

robot = Robot(model, semantics=semantics)
print(robot.get_end_effector_link_name())
print(model)
