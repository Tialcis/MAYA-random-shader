from maya import cmds
import random

class RandomShader():

    def __init__(self):
        self.objects_to_shade = []
        self.shaders_to_apply = []
        self.SHADER_RAINBOW = [ 'RED',
                                'ORANGE',
                                'YELLOW',
                                'GREEN',
                                'BLUE',
                                'INDIGO',
                                'VIOLET']
        self.shader_counter = [0, 0, 0, 0, 0, 0, 0]

    def bake_objects(self):
        """
        Saves the selected objects random shading
        """

        selected_objects = cmds.ls(sl=True)
        del self.objects_to_shade[:]
        for obj in selected_objects:
            self.objects_to_shade.append(obj)
        print self.objects_to_shade

    def bake_shaders(self):
        """
        Saves the selected shaders to apply to objects
        """

        selected_shaders = cmds.ls(sl=True)
        del self.shaders_to_apply[:]
        for shdr in selected_shaders:
            self.shaders_to_apply.append(shdr)
        print self.shaders_to_apply

    def assign_randomly(self):
        number_of_shaders = len(self.shaders_to_apply)
        for obj in self.objects_to_shade:
            rand_number = random.randint(0, number_of_shaders-1)
            cmds.select(obj)
            shader_name = self.shaders_to_apply[rand_number]
            self._assign_selection_to_shader(shader_name)
        cmds.select(clear=True)

    def assign_distribution(self):
        number_of_shaders = 7
        for obj in self.objects_to_shade:
            rand_number = random.randint(0, 10001)
            cmds.select(obj)
            shader_name = self._distribute_shader(rand_number)
            self._assign_selection_to_shader(shader_name)
            print shader_name
        cmds.select(clear=True)

    def _get_SG_from_shader(self, shader=None):
        if shader:
            if cmds.objExists(shader):
                shading_group_query = cmds.listConnections(shader, destination=True, exactType=True, type='shadingEngine')
                if shading_group_query:
                    return shading_group_query[0]

        return None

    def _assign_obj_list_to_shader(self, obj_list=None, shader=None):

        """
        Assign the shader to the object list
        :param obj_list: list of objects or faces
        :param shader: set shader to apply to objects
        """

        shader_SG = self._get_SG_from_shader(shader)
        if obj_list:
            if shader_SG:
                cmds.sets(obj_list, e=True, forceElement=shader_SG)
            else:
                print 'The provided shader %s didn\'t return a shader_SG' % shader
        else:
            print 'Please select one or more objects'

    def _assign_selection_to_shader(self, shader=None):
        sel = cmds.ls(sl=True, long=True)
        if sel:
            self._assign_obj_list_to_shader(sel, shader)

    def _distribute_shader(self, rand_number):
        """
        Determines shader in normal distribution for ROYGBIV
        :param rand_number (int): number used to randomly place within normal curve of shaders
        :return (str): a string representing a shader in the rainbow
        """
        if (0 < rand_number <= 475):
            self.shader_counter[0]+=1
            return self.SHADER_RAINBOW[0]
        elif (475 < rand_number <= 1595):
            self.shader_counter[1]+=1
            return self.SHADER_RAINBOW[1]
        elif (1595 < rand_number <= 3710):
            self.shader_counter[2]+=1
            return self.SHADER_RAINBOW[2]
        elif (3710 < rand_number <= 6290):
            self.shader_counter[3]+=1
            return self.SHADER_RAINBOW[3]
        elif (6290 < rand_number <= 8405):
            self.shader_counter[4]+=1
            return self.SHADER_RAINBOW[4]
        elif (8405 < rand_number <= 9525):
            self.shader_counter[5]+=1
            return self.SHADER_RAINBOW[5]
        elif (9525 < rand_number <= 10000):
            self.shader_counter[6]+=1
            return self.SHADER_RAINBOW[6]
