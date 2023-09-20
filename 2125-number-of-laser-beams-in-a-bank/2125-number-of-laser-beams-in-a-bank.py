class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n_devices = []
        
        for row in bank:
            device_per_layer = 0
            for char in row:
                if char == '1':
                    device_per_layer += 1
            
            if device_per_layer > 0:
                n_devices.append(device_per_layer)
        
        
        laser_count = 0
        
        for i in range(1, len(n_devices)):
            laser_count += n_devices[i - 1] * n_devices[i]
        
        return laser_count