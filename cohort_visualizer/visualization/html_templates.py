"""
HTML template module for generating the dashboard components.
"""

# Base HTML template for the dashboard
BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cohort Visualizer - {cohort_name}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.11.5/css/dataTables.bootstrap5.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.7.1/dist/chart.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/d3@7.8.4/dist/d3.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.5/js/dataTables.bootstrap5.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns@2.0.0/dist/chartjs-adapter-date-fns.bundle.min.js"></script>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding-top: 56px;
            background-color: #f8f9fa;
        }}
        .dashboard-container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        .card {{
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            margin-bottom: 20px;
            border: none;
        }}
        .card-header {{
            background-color: #f8f9fa;
            border-bottom: 1px solid #eaeaea;
            font-weight: 600;
            color: #333;
        }}
        .chart-container {{
            height: 400px;
            width: 100%;
            position: relative;
        }}
        .summary-box {{
            background-color: #ffffff;
            border-left: 4px solid #0d6efd;
            border-radius: 4px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }}
        .summary-value {{
            font-size: 1.8rem;
            font-weight: 700;
        }}
        .summary-label {{
            font-size: 0.9rem;
            color: #6c757d;
            text-transform: uppercase;
        }}
        .phase-badge {{
            padding: 5px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: 600;
        }}
        .mouse-timeline {{
            margin-bottom: 20px;
        }}
        table.dataTable {{
            width: 100% !important;
        }}
        .heatmap-cell {{
            stroke: #fff;
            stroke-width: 1px;
        }}
        .mouse-selector {{
            margin-bottom: 15px;
        }}
        .filter-container {{
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            border: 1px solid #eaeaea;
        }}
        .tab-content {{
            padding-top: 20px;
        }}
        .dataTables_wrapper {{
            padding: 15px;
        }}
        .page-section {{
            padding-top: 30px;
            padding-bottom: 30px;
        }}
        .section-title {{
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid #dee2e6;
        }}
        /* Custom colors for phases */
        .phase-1 {{ background-color: #007bff; color: white; }}
        .phase-2 {{ background-color: #28a745; color: white; }}
        .phase-3 {{ background-color: #17a2b8; color: white; }}
        .phase-4 {{ background-color: #ffc107; color: black; }}
        .phase-5 {{ background-color: #dc3545; color: white; }}
        .phase-6 {{ background-color: #6610f2; color: white; }}
        .phase-7 {{ background-color: #fd7e14; color: white; }}
        .phase-8 {{ background-color: #20c997; color: white; }}
        .phase-9 {{ background-color: #e83e8c; color: white; }}
        .phase-10 {{ background-color: #6f42c1; color: white; }}
        /* For variants like 3b */
        .phase-3b {{ background-color: #138496; color: white; }}
        .phase-4b {{ background-color: #d39e00; color: black; }}
        /* Test phase */
        .phase-test {{ background-color: #6c757d; color: white; }}
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <i class="bi bi-bar-chart-line"></i> Cohort Visualizer
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#overview">Overview</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#timeline">Timeline</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#mouse-analysis">Mouse Analysis</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#phase-analysis">Phase Analysis</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#session-explorer">Session Explorer</a>
                    </li>
                </ul>
                <span class="navbar-text">
                    <i class="bi bi-calendar-check"></i> {date_generated}
                </span>
            </div>
        </div>
    </nav>

    <div class="container-fluid dashboard-container">
        <!-- Overview Section -->
        <section id="overview" class="page-section">
            <h2 class="section-title">
                <i class="bi bi-speedometer2"></i> Cohort Overview: {cohort_name}
            </h2>
            <div class="row">
                <div class="col-md-3">
                    <div class="summary-box">
                        <div class="summary-value">{total_mice}</div>
                        <div class="summary-label">Total Mice</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="summary-box">
                        <div class="summary-value">{total_sessions}</div>
                        <div class="summary-label">Total Sessions</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="summary-box">
                        <div class="summary-value">{date_range_start}</div>
                        <div class="summary-label">First Session</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="summary-box">
                        <div class="summary-value">{date_range_end}</div>
                        <div class="summary-label">Last Session</div>
                    </div>
                </div>
            </div>
            <div class="row mt-4">
                <div class="col-md-6">
                    <div class="card">
                        <div class="card-header">
                            <i class="bi bi-calendar-week"></i> Session Activity
                        </div>
                        <div class="card-body">
                            <div class="chart-container">
                                <canvas id="activityChart"></canvas>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card">
                        <div class="card-header">
                            <i class="bi bi-list-nested"></i> Phase Distribution
                        </div>
                        <div class="card-body">
                            <div class="chart-container">
                                <canvas id="phaseDistributionChart"></canvas>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Timeline Section -->
        <section id="timeline" class="page-section">
            <h2 class="section-title">
                <i class="bi bi-calendar-range"></i> Experiment Timeline
            </h2>
            <div class="card">
                <div class="card-header">
                    <i class="bi bi-grid-3x3"></i> Session Heatmap
                </div>
                <div class="card-body">
                    <div class="filter-container">
                        <div class="row align-items-center">
                            <div class="col-md-6">
                                <label for="monthSelector" class="form-label">Month Range:</label>
                                <select id="monthSelector" class="form-select">
                                    <option value="all">All Data</option>
                                    {month_options}
                                </select>
                            </div>
                            <div class="col-md-6">
                                <label for="mouseFilterHeatmap" class="form-label">Filter Mice:</label>
                                <select id="mouseFilterHeatmap" class="form-select" multiple>
                                    <option value="all" selected>All Mice</option>
                                    {mouse_options}
                                </select>
                            </div>
                        </div>
                    </div>
                    <div id="heatmapContainer" style="width: 100%; height: 500px;"></div>
                </div>
            </div>
            
            <div class="card mt-4">
                <div class="card-header">
                    <i class="bi bi-graph-up"></i> Weekly Session Activity
                </div>
                <div class="card-body">
                    <div class="chart-container">
                        <canvas id="weeklyActivityChart"></canvas>
                    </div>
                </div>
            </div>
        </section>

        <!-- Mouse Analysis Section -->
        <section id="mouse-analysis" class="page-section">
            <h2 class="section-title">
                <i class="bi bi-mouse2"></i> Mouse Analysis
            </h2>
            <div class="filter-container">
                <div class="row">
                    <div class="col-md-6">
                        <label for="mouseSelector" class="form-label">Select Mouse:</label>
                        <select id="mouseSelector" class="form-select">
                            {mouse_options_single}
                        </select>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <div class="card-header">
                    <i class="bi bi-arrow-up-right"></i> Phase Progression
                </div>
                <div class="card-body">
                    <div class="chart-container">
                        <canvas id="mouseProgressionChart"></canvas>
                    </div>
                </div>
            </div>
            
            <div class="card mt-4">
                <div class="card-header">
                    <i class="bi bi-calendar-date"></i> Session Calendar
                </div>
                <div class="card-body">
                    <div id="mouseCalendarContainer" style="width: 100%;"></div>
                </div>
            </div>
            
            <div class="card mt-4">
                <div class="card-header">
                    <i class="bi bi-list-check"></i> Mouse Sessions
                </div>
                <div class="card-body">
                    <table id="mouseSessionsTable" class="table table-striped table-hover">
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Time</th>
                                <th>Session ID</th>
                                <th>Phase</th>
                                <th>Trials</th>
                                <th>Video Length</th>
                            </tr>
                        </thead>
                        <tbody id="mouseSessionsTableBody">
                            <!-- Data will be populated with JavaScript -->
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- Phase Analysis Section -->
        <section id="phase-analysis" class="page-section">
            <h2 class="section-title">
                <i class="bi bi-diagram-3"></i> Phase Analysis
            </h2>
            <div class="filter-container">
                <div class="row">
                    <div class="col-md-6">
                        <label for="phaseSelector" class="form-label">Select Phase:</label>
                        <select id="phaseSelector" class="form-select">
                            {phase_options}
                        </select>
                    </div>
                </div>
            </div>
            
            <div class="row">
                <div class="col-md-6">
                    <div class="card">
                        <div class="card-header">
                            <i class="bi bi-pie-chart"></i> Mice Distribution by Phase
                        </div>
                        <div class="card-body">
                            <div class="chart-container">
                                <canvas id="phaseDistributionByMiceChart"></canvas>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card">
                        <div class="card-header">
                            <i class="bi bi-calendar-plus"></i> Phase Timeline
                        </div>
                        <div class="card-body">
                            <div class="chart-container">
                                <canvas id="phaseTimelineChart"></canvas>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="card mt-4">
                <div class="card-header">
                    <i class="bi bi-table"></i> Phase Sessions
                </div>
                <div class="card-body">
                    <table id="phaseSessionsTable" class="table table-striped table-hover">
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Time</th>
                                <th>Mouse</th>
                                <th>Session ID</th>
                                <th>Trials</th>
                                <th>Video Length</th>
                            </tr>
                        </thead>
                        <tbody id="phaseSessionsTableBody">
                            <!-- Data will be populated with JavaScript -->
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- Session Explorer Section -->
        <section id="session-explorer" class="page-section">
            <h2 class="section-title">
                <i class="bi bi-search"></i> Session Explorer
            </h2>
            <div class="filter-container">
                <div class="row">
                    <div class="col-md-4">
                        <label for="dateFilter" class="form-label">Date Range:</label>
                        <div class="input-group">
                            <input type="date" id="startDateFilter" class="form-control" value="{default_start_date}">
                            <span class="input-group-text">to</span>
                            <input type="date" id="endDateFilter" class="form-control" value="{default_end_date}">
                        </div>
                    </div>
                    <div class="col-md-4">
                        <label for="mouseFilter" class="form-label">Filter Mice:</label>
                        <select id="mouseFilter" class="form-select" multiple>
                            <option value="all" selected>All Mice</option>
                            {mouse_options}
                        </select>
                    </div>
                    <div class="col-md-4">
                        <label for="phaseFilter" class="form-label">Filter Phases:</label>
                        <select id="phaseFilter" class="form-select" multiple>
                            <option value="all" selected>All Phases</option>
                            {phase_options_all}
                        </select>
                    </div>
                </div>
                <div class="row mt-3">
                    <div class="col-12">
                        <button id="applyFilters" class="btn btn-primary">Apply Filters</button>
                        <button id="resetFilters" class="btn btn-secondary ms-2">Reset Filters</button>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <div class="card-header">
                    <i class="bi bi-table"></i> All Sessions
                </div>
                <div class="card-body">
                    <table id="allSessionsTable" class="table table-striped table-hover">
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Time</th>
                                <th>Mouse</th>
                                <th>Session ID</th>
                                <th>Phase</th>
                                <th>Trials</th>
                                <th>Video Length</th>
                                <th>Details</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Data will be populated with JavaScript -->
                        </tbody>
                    </table>
                </div>
            </div>
            
            <!-- Session Details Modal -->
            <div class="modal fade" id="sessionDetailsModal" tabindex="-1" aria-hidden="true">
                <div class="modal-dialog modal-lg">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="sessionModalLabel">Session Details</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body" id="sessionModalBody">
                            <!-- Will be filled dynamically -->
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>

    <footer class="bg-dark text-light py-4 mt-5">
        <div class="container text-center">
            <p>Generated with Cohort Visualizer on {date_generated}</p>
            <p><small>Data from: {cohort_directory}</small></p>
        </div>
    </footer>
"""

# JavaScript part of the template (truncated for brevity)
JAVASCRIPT_TEMPLATE = """
    <script>
        // Data loading and initialization code here...
    </script>
</body>
</html>
"""

def generate_html_template(cohort_meta, date_generated, cohort_directory):
    """
    Generates the full HTML template with the appropriate placeholders filled in.
    
    Args:
        cohort_meta: Dictionary containing cohort metadata
        date_generated: Date string when the dashboard was generated
        cohort_directory: Path to the cohort directory
        
    Returns:
        Complete HTML template as a string
    """
    from datetime import datetime
    
    # Extract metadata
    cohort_name = cohort_meta.get("cohort_name", "Unknown Cohort")
    total_mice = cohort_meta.get("total_mice", 0)
    total_sessions = cohort_meta.get("total_sessions", 0)
    
    # Format date range
    date_range = cohort_meta.get("date_range", [None, None])
    date_range_start = date_range[0] if date_range[0] else "N/A"
    date_range_end = date_range[1] if date_range[1] else "N/A"
    
    # Generate mouse options for dropdowns
    mice_list = cohort_meta.get("mice_list", [])
    mouse_options = "\n".join([f'<option value="{mouse}">{mouse}</option>' for mouse in mice_list])
    mouse_options_single = "\n".join([f'<option value="{mouse}">{mouse}</option>' for mouse in mice_list])
    
    # Generate phase options
    # This should be dynamic based on actual phases in your data
    phase_list = ["1", "2", "3", "3b", "4", "4b", "5", "6", "7", "8", "9", "9b", "9c", "10", "test"]
    phase_options = "\n".join([f'<option value="{phase}">Phase {phase}</option>' for phase in phase_list])
    phase_options_all = "\n".join([f'<option value="{phase}">Phase {phase}</option>' for phase in phase_list])
    
    # Generate month options
    # This should be dynamic based on your date range
    month_options = ""
    if date_range[0] and date_range[1]:
        try:
            start_date = datetime.strptime(date_range[0], "%Y-%m-%d")
            end_date = datetime.strptime(date_range[1], "%Y-%m-%d")
            
            current_month = datetime(start_date.year, start_date.month, 1)
            while current_month <= end_date:
                month_name = current_month.strftime("%B %Y")
                month_value = current_month.strftime("%Y-%m")
                month_options += f'<option value="{month_value}">{month_name}</option>\n'
                
                # Move to next month
                if current_month.month == 12:
                    current_month = datetime(current_month.year + 1, 1, 1)
                else:
                    current_month = datetime(current_month.year, current_month.month + 1, 1)
        except:
            # Fallback if date parsing fails
            month_options = "<option value='all'>All Months</option>"
    
    # Default date range for filters
    default_start_date = date_range[0] if date_range[0] else ""
    default_end_date = date_range[1] if date_range[1] else ""
    
    # Format the template with the data
    template = BASE_TEMPLATE.format(
        cohort_name=cohort_name,
        date_generated=date_generated,
        total_mice=total_mice,
        total_sessions=total_sessions,
        date_range_start=date_range_start,
        date_range_end=date_range_end,
        mouse_options=mouse_options,
        mouse_options_single=mouse_options_single,
        phase_options=phase_options,
        phase_options_all=phase_options_all,
        month_options=month_options,
        default_start_date=default_start_date,
        default_end_date=default_end_date,
        cohort_directory=str(cohort_directory)
    )
    
    # For simplicity, we're using a simplified JAVASCRIPT_TEMPLATE here
    # You should replace this with your full JavaScript code if needed
    return template