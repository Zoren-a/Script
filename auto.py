import re
import os
import sys
import math

def Config(SM, MM, shader, shared, core, dl1, l1latency, dl2):
    SM_cluster = SM
    MM_cluster = MM
    shader_cluster = shader
    shared_cluster = shared
    dl1_cluster = dl1
    core_num = core
    l1latency_cluster = l1latency
    dl2_cluster = dl2
    K_num = math.isqrt(SM_cluster+MM_cluster)

    with open('gpgpusim.config.bak', mode='r') as in_file, \
        open('gpgpusim.config', mode='w') as out_file:

        for line in in_file:
            x = re.search("^#", line)
            if x:
                out_file.write(f'{x.string}')
            else:
                if re.search("^-gpgpu_n_clusters ", line):
                    SM_name, SM_number = line.split()
                    out_file.write(f'{SM_name}'+' '+ f'{SM_cluster}\n')
                elif re.search("^-gpgpu_n_mem ", line):
                    MM_name, MM_number = line.split()
                    out_file.write(f'{MM_name}'+' '+ f'{MM_cluster}\n')
                elif re.search("^-gpgpu_shader_registers ", line):
                    shader_name, shader_number = line.split()
                    out_file.write(f'{shader_name}'+' '+ f'{shader_cluster}\n')
                elif re.search("^-gpgpu_shmem_size ", line):
                    shared_name, shared_number = line.split()
                    out_file.write(f'{shared_name}'+' '+ f'{shared_cluster}\n')
                elif re.search("^-gpgpu_shader_core_pipeline ", line):
                    core_name, core_number = line.split()
                    out_file.write(f'{core_name}'+' '+ f'{core_num}\n')
                elif re.search("^-gpgpu_cache:dl1 ", line):
                    dl1_name, dl1_number = line.split()
                    x = dl1_number.split(',')
                    x[0] = dl1_cluster
                    out_file.write(f'{dl1_name}'+' '+ ','.join(x) + '\n')
                elif re.search("^-gpgpu_l1_latency ", line):
                    l1latency_name, l1latency_number = line.split()
                    out_file.write(f'{l1latency_name}'+' '+ f'{l1latency_cluster}\n')
                elif re.search("^-gpgpu_cache:dl2 ", line):
                    dl2_name, dl2_number = line.split()
                    x = dl2_number.split(',')
                    x[0] = dl2_cluster
                    out_file.write(f'{dl2_name}'+' '+ ','.join(x) + '\n')
                else:
                    out_file.write(f'{line}')

    with open('config_fermi_islip.icnt.bak', mode='r') as in_file, \
        open('config_fermi_islip.icnt', mode='w') as out_file:

        for line in in_file:
            x = re.search("^/", line)
            if x:
                out_file.write(f'{x.string}')
            else:
                if re.search("^k = ", line):
                    SM_name, SM_equal, SM_number = line.split()
                    out_file.write(f'{SM_name}'+' '+ f'{SM_equal}'+ ' ' + f'{K_num};\n')
                else:
                    out_file.write(f'{line}')

SM = int(sys.argv[1])
MM = int(sys.argv[2])
shader = int(sys.argv[3])*1024
shared = int(sys.argv[4])*1024
core = sys.argv[5]
dl1 = sys.argv[6]
l1latency = int(sys.argv[7])
dl2 = sys.argv[8]
Config(SM, MM, shader, shared, core, dl1, l1latency, dl2)

# Config(4, 4, 16384, '2048:32', 8, 82, 'S:128:256:16')
#cmd = './ispass-2009-BFS data/graph4096.txt'
#os.system(cmd)
# 2048:32 
# 1024:32
# 1536:32 