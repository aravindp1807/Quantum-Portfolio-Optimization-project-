# main.py - runs entire pipeline
import sys
import os

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

if __name__ == "__main__":
    print("=" * 80)
    print("RUNNING FULL QUANTUM PORTFOLIO OPTIMIZATION PIPELINE")
    print("=" * 80)

    print("\n--- PHASE 1: DATA PREPARATION & QUBO FORMULATION ---")
    import src.phase1_data_preparation

    print("\n--- PHASE 2: CLASSICAL BASELINE OPTIMIZATION ---")
    import src.phase2_classical_baseline
    src.phase2_classical_baseline.main()

    print("\n--- PHASE 3: QUBO VALIDATION & ISING MAPPING ---")
    import src.phase3_qubo_validation
    src.phase3_qubo_validation.main()

    print("\n--- PHASE 4: QAOA OPTIMIZATION & QUANTUM EXECUTION ---")
    import src.phase4_qaoa_optimization
    src.phase4_qaoa_optimization.main()
