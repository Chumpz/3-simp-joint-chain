import maya.cmds as cmds


def selected_object_positions():
    positions = []
    
    selection = cmds.ls(selection=True)
    for obj in selection:
        positions.append(cmds.xform(obj, query=True, worldSpace=True, translation=True))
    
    return positions

def create_ik_arm(joint_positions):
    if len(joint_positions) < 3:
        raise RuntimeError("Expected 3 joint positions")
        
    cmds.select(clear=True)

    shoulder_jnt = cmds.joint(position=joint_positions[0], name="shoulder_jnt")
    elbow_jnt = cmds.joint(position=joint_positions[1], name="elbow_jnt")
    wrist_jnt = cmds.joint(position=joint_positions[2], name="wrist_jnt")

    cmds.joint(shoulder_jnt, edit=True, orientJoint="xyz", zeroScaleOrient=True, secondaryAxisOrient="yup")
    cmds.joint(elbow_jnt, edit=True, orientJoint="xyz", zeroScaleOrient=True, secondaryAxisOrient="yup")

    cmds.ikHandle(startJoint=shoulder_jnt, endEffector=wrist_jnt)

if __name__ == "__main__":
    
    joint_positions = selected_object_positions()
    
    create_ik_arm(joint_positions)