"""
Generate dashboard script.

This script creates an interactive HTML dashboard for visualizing cohort data.
All configuration is done through variables in the code.
"""

import sys
import os
from pathlib import Path

# Add the parent directory to the path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cohort_visualizer.core.cohort_date_organizer import CohortDateOrganizer
from cohort_visualizer.visualization.dashboard_generator import DashboardGenerator
from cohort_visualizer.utils.file_utils import open_html_file


def main():
    """
    Main function to generate the dashboard.
    
    Configuration is defined through variables in this function rather than
    command-line arguments.
    """
    # =====================================================
    # CONFIGURATION VARIABLES - Modify these as needed
    # =====================================================
    
    # Path to your cohort directory containing session data
    # Replace this with your actual cohort directory path
    COHORT_DIRECTORY = "D:/Data/September_portable"
    
    # Directory to save the dashboard (set to None to use cohort_directory/dashboard)
    OUTPUT_DIR = None
    
    # Whether the data is split across multiple mouse folders
    MULTI = True
    
    # Whether to use portable data format vs. full raw-data logic
    PORTABLE_DATA = True
    
    # Whether to open the dashboard in a browser after generation
    OPEN_IN_BROWSER = True
    
    # Whether to use existing cohort_info.json if available
    USE_EXISTING_COHORT_INFO = True
    
    # Whether to generate plots during cohort organization
    GENERATE_PLOTS = False
    
    # =====================================================
    # End of configuration variables
    # =====================================================
    
    print(f"Generating dashboard for cohort: {COHORT_DIRECTORY}")
    
    # Create the cohort date organizer
    cohort_organizer = CohortDateOrganizer(
        COHORT_DIRECTORY,
        multi=MULTI,
        portable_data=PORTABLE_DATA,
        use_existing_cohort_info=USE_EXISTING_COHORT_INFO,
        plot=GENERATE_PLOTS
    )
    
    # Create the dashboard generator
    dashboard_generator = DashboardGenerator(cohort_organizer)
    
    # Generate the dashboard
    if not OUTPUT_DIR:
        output_dir = Path(COHORT_DIRECTORY) / "dashboard"
    else:
        output_dir = Path(OUTPUT_DIR)
    
    dashboard_path = dashboard_generator.generate_dashboard(output_dir)
    
    print(f"Dashboard generated at: {dashboard_path}")
    
    # Open the dashboard in a browser if requested
    if OPEN_IN_BROWSER:
        print("Opening dashboard in browser...")
        if not open_html_file(dashboard_path):
            print("Failed to open dashboard in browser. Please open manually.")
            print(f"Path to dashboard: {dashboard_path}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())