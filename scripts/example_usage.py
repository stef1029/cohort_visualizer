"""
Simplified dashboard generator script.

This script takes a cohort directory and generates an interactive HTML dashboard.
Just modify the variables at the top of the script and run it.
"""

import os
import sys
from pathlib import Path

# Add the parent directory to the path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cohort_visualizer.core.cohort_date_organizer import CohortDateOrganizer
from cohort_visualizer.visualization.dashboard_generator import DashboardGenerator


def generate_dashboard(cohort_directory, 
                      multi=True, 
                      portable_data=True, 
                      use_existing_cohort_info=True,
                      output_dir=None,
                      open_browser=True):
    """
    Generate an interactive dashboard for the specified cohort directory.
    
    Args:
        cohort_directory: Path to the cohort directory containing session data
        multi: Whether the data is split across multiple mouse folders
        portable_data: Whether to use portable data format vs. full raw-data logic
        use_existing_cohort_info: Whether to use existing cohort_info.json if available
        output_dir: Directory to save the dashboard (default: cohort_directory/dashboard)
        open_browser: Whether to open the dashboard in a browser after generation
        
    Returns:
        Path to the generated dashboard HTML file
    """
    # Convert string path to Path object if needed
    cohort_directory = Path(cohort_directory)
    
    print(f"Initialising cohort organiser for: {cohort_directory}")
    
    # Initialise the cohort organiser
    cohort_organiser = CohortDateOrganizer(
        cohort_directory,
        multi=multi,
        portable_data=portable_data,
        use_existing_cohort_info=use_existing_cohort_info,
        plot=False  # Don't create the default cohort info plot
    )
    
    print("Generating interactive dashboard...")
    
    # Create dashboard generator
    dashboard_generator = DashboardGenerator(cohort_organiser)
    
    # Generate the dashboard
    if output_dir is None:
        output_dir = cohort_directory / "dashboard"
    
    dashboard_path = dashboard_generator.generate_dashboard(output_dir)
    
    print(f"Dashboard generated successfully at: {dashboard_path}")
    
    # Open the dashboard in a browser if requested
    if open_browser:
        print("Opening dashboard in web browser...")
        dashboard_generator.open_dashboard()
    
    return dashboard_path


def main():
    """
    Main function to generate a dashboard using the defined variables.
    """
    # =====================================================
    # CONFIGURATION VARIABLES - Modify these as needed
    # =====================================================
    
    # Path to your cohort directory containing session data
    # Replace this with your actual cohort directory path
    COHORT_DIRECTORY = "D:/Data/September_portable"
    
    # Whether the data is split across multiple mouse folders
    MULTI = True
    
    # Whether to use portable data format vs. full raw-data logic
    PORTABLE_DATA = True
    
    # Whether to use existing cohort_info.json if available
    USE_EXISTING_COHORT_INFO = True
    
    # Directory to save the dashboard (leave as None to use cohort_directory/dashboard)
    OUTPUT_DIR = None
    
    # Whether to open the dashboard in a browser after generation
    OPEN_BROWSER = True
    
    # =====================================================
    # End of configuration variables
    # =====================================================
    
    # Generate the dashboard with the configured settings
    dashboard_path = generate_dashboard(
        cohort_directory=COHORT_DIRECTORY,
        multi=MULTI,
        portable_data=PORTABLE_DATA,
        use_existing_cohort_info=USE_EXISTING_COHORT_INFO,
        output_dir=OUTPUT_DIR,
        open_browser=OPEN_BROWSER
    )
    
    print(f"Dashboard generation complete! View your dashboard at: {dashboard_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())