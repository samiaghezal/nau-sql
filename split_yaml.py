import yaml
import os
from pathlib import Path

def split_yaml_file(input_file, max_paths_per_file=100):
    """
    Split a large OpenAPI YAML file into smaller chunks
    
    Args:
        input_file (str): Path to input YAML file
        max_paths_per_file (int): Maximum number of paths per output file
    """
    # Read the original YAML file
    with open(input_file, 'r') as f:
        spec = yaml.safe_load(f)
    
    # Create output directory
    output_dir = Path('split_specs')
    output_dir.mkdir(exist_ok=True)
    
    # Keep the base structure (everything except paths)
    base_spec = {k:v for k,v in spec.items() if k != 'paths'}
    
    # Split paths into chunks
    paths = spec.get('paths', {})
    path_items = list(paths.items())
    total_paths = len(path_items)
    
    for i in range(0, total_paths, max_paths_per_file):
        chunk_paths = dict(path_items[i:i + max_paths_per_file])
        
        # Create new spec for this chunk
        chunk_spec = base_spec.copy()
        chunk_spec['paths'] = chunk_paths
        
        # Generate output filename
        chunk_num = (i // max_paths_per_file) + 1
        output_file = output_dir / f'spec_chunk_{chunk_num}.yaml'
        
        # Write chunk to file
        with open(output_file, 'w') as f:
            yaml.dump(chunk_spec, f, sort_keys=False)
        
        print(f'Generated {output_file} with {len(chunk_paths)} paths')
        print(f'Progress: {min(i + max_paths_per_file, total_paths)}/{total_paths} paths processed')

def merge_yaml_files(input_dir, output_file):
    """
    Merge split YAML files back into a single file
    
    Args:
        input_dir (str): Directory containing split YAML files
        output_file (str): Path for merged output file
    """
    merged_spec = None
    input_path = Path(input_dir)
    
    # Read and merge all chunk files
    for chunk_file in sorted(input_path.glob('spec_chunk_*.yaml')):
        with open(chunk_file, 'r') as f:
            chunk_spec = yaml.safe_load(f)
            
            if merged_spec is None:
                merged_spec = chunk_spec
            else:
                # Merge paths from this chunk
                merged_spec['paths'].update(chunk_spec.get('paths', {}))
    
    # Write merged spec to file
    if merged_spec:
        with open(output_file, 'w') as f:
            yaml.dump(merged_spec, f, sort_keys=False)
        print(f'Successfully merged specs into {output_file}')

if __name__ == '__main__':
    # Example usage
    input_file = 'stripe.yaml'  # Your large YAML file
    
    # Split the file
    split_yaml_file(input_file, max_paths_per_file=50)
    
    # Optionally merge back
    # merge_yaml_files('split_specs', 'merged_spec.yaml')
