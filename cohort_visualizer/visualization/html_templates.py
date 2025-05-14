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
        // Global variables to store data
        let activityData = [];
        let phaseDistributionData = [];
        let mouseHeatmapData = [];
        let mouseProgressionData = [];
        let weeklyData = [];
        let sessionDetailsData = [];
        let cohortMetadata = {};
        
        // Charts 
        let activityChart;
        let phaseDistributionChart;
        let weeklyActivityChart;
        let mouseProgressionChart;
        let phaseDistributionByMiceChart;
        let phaseTimelineChart;
        
        // DOM Elements
        const mouseSelector = document.getElementById('mouseSelector');
        const phaseSelector = document.getElementById('phaseSelector');
        const monthSelector = document.getElementById('monthSelector');
        const mouseFilterHeatmap = document.getElementById('mouseFilterHeatmap');
        
        // Load all data when the document is ready
        document.addEventListener('DOMContentLoaded', function() {
            // Load all JSON data files
            Promise.all([
                fetch('dashboard_data/date_activity.json').then(response => response.json()),
                fetch('dashboard_data/phase_distribution.json').then(response => response.json()),
                fetch('dashboard_data/mouse_heatmap.json').then(response => response.json()),
                fetch('dashboard_data/mouse_progression.json').then(response => response.json()),
                fetch('dashboard_data/weekly_summary.json').then(response => response.json()),
                fetch('dashboard_data/session_details.json').then(response => response.json()),
                fetch('dashboard_data/cohort_metadata.json').then(response => response.json())
            ]).then(([activity, phase, heatmap, progression, weekly, sessions, metadata]) => {
                // Store data in global variables
                activityData = activity;
                phaseDistributionData = phase;
                mouseHeatmapData = heatmap;
                mouseProgressionData = progression;
                weeklyData = weekly;
                sessionDetailsData = sessions;
                cohortMetadata = metadata;
                
                // Initialize all visualizations
                initializeCharts();
                createHeatmap();
                initializeSessionTables();
                
                // Setup event listeners for filters and selectors
                setupEventListeners();
            }).catch(error => {
                console.error('Error loading data:', error);
                alert('Failed to load dashboard data. See console for details.');
            });
        });
        
        // Initialize all charts
        function initializeCharts() {
            // Activity Chart
            const activityCtx = document.getElementById('activityChart').getContext('2d');
            activityChart = new Chart(activityCtx, {
                type: 'bar',
                data: {
                    labels: activityData.map(d => d.Date),
                    datasets: [{
                        label: 'Number of Sessions',
                        data: activityData.map(d => d.Sessions),
                        backgroundColor: 'rgba(54, 162, 235, 0.5)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Number of Sessions'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        }
                    }
                }
            });
            
            // Phase Distribution Chart
            const phaseCtx = document.getElementById('phaseDistributionChart').getContext('2d');
            const phaseColors = getPhaseColors(phaseDistributionData.map(d => d.Phase));
            
            phaseDistributionChart = new Chart(phaseCtx, {
                type: 'pie',
                data: {
                    labels: phaseDistributionData.map(d => `Phase ${d.Phase}`),
                    datasets: [{
                        data: phaseDistributionData.map(d => d.Sessions),
                        backgroundColor: phaseColors
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'right'
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    const label = context.label || '';
                                    const value = context.raw || 0;
                                    const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                    const percentage = Math.round((value / total) * 100);
                                    return `${label}: ${value} sessions (${percentage}%)`;
                                }
                            }
                        }
                    }
                }
            });
            
            // Weekly Activity Chart
            const weeklyCtx = document.getElementById('weeklyActivityChart').getContext('2d');
            weeklyActivityChart = new Chart(weeklyCtx, {
                type: 'line',
                data: {
                    labels: weeklyData.map(d => d.WeekLabel),
                    datasets: [{
                        label: 'Sessions per Week',
                        data: weeklyData.map(d => d.Sessions),
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 2,
                        tension: 0.1,
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Number of Sessions'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Week'
                            }
                        }
                    }
                }
            });
            
            // Initialize mouse progression chart (empty until mouse is selected)
            const mouseProgressionCtx = document.getElementById('mouseProgressionChart').getContext('2d');
            mouseProgressionChart = new Chart(mouseProgressionCtx, {
                type: 'scatter',
                data: {
                    datasets: []
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            title: {
                                display: true,
                                text: 'Phase'
                            }
                        },
                        x: {
                            type: 'time',
                            time: {
                                unit: 'day'
                            },
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        }
                    }
                }
            });
            
            // Initialize other charts for phase analysis
            initializePhaseCharts();
        }
        
        // Initialize phase-specific charts
        function initializePhaseCharts() {
            // Phase Distribution by Mice Chart
            const phaseDistByMiceCtx = document.getElementById('phaseDistributionByMiceChart').getContext('2d');
            phaseDistributionByMiceChart = new Chart(phaseDistByMiceCtx, {
                type: 'doughnut',
                data: {
                    labels: [],
                    datasets: [{
                        data: [],
                        backgroundColor: []
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'right'
                        }
                    }
                }
            });
            
            // Phase Timeline Chart
            const phaseTimelineCtx = document.getElementById('phaseTimelineChart').getContext('2d');
            phaseTimelineChart = new Chart(phaseTimelineCtx, {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [{
                        label: 'Sessions',
                        data: [],
                        backgroundColor: 'rgba(153, 102, 255, 0.2)',
                        borderColor: 'rgba(153, 102, 255, 1)',
                        borderWidth: 2,
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Number of Sessions'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        }
                    }
                }
            });
        }
        
        // Create heatmap visualization
        function createHeatmap() {
            const margin = {top: 30, right: 30, bottom: 100, left: 100};
            const width = 1000 - margin.left - margin.right;
            const height = 500 - margin.top - margin.bottom;
            
            // Clear existing heatmap
            d3.select("#heatmapContainer").html("");
            
            // Create SVG
            const svg = d3.select("#heatmapContainer")
              .append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
              .append("g")
                .attr("transform", `translate(${margin.left},${margin.top})`);
            
            // Get unique dates and mice
            const dates = [...new Set(mouseHeatmapData.map(d => d.Date))].sort();
            const mice = [...new Set(mouseHeatmapData.map(d => d.index))];
            
            // Build X and Y scales
            const x = d3.scaleBand()
              .range([0, width])
              .domain(mice)
              .padding(0.05);
            
            const y = d3.scaleBand()
              .range([0, height])
              .domain(dates)
              .padding(0.05);
            
            // Add X and Y axis labels
            svg.append("g")
              .style("font-size", 15)
              .attr("transform", `translate(0,${height})`)
              .call(d3.axisBottom(x).tickSize(0))
              .selectAll("text")
                .attr("transform", "translate(-10,0)rotate(-45)")
                .style("text-anchor", "end");
            
            svg.append("g")
              .style("font-size", 15)
              .call(d3.axisLeft(y).tickSize(0));
            
            // Build color scale
            const maxValue = d3.max(mouseHeatmapData, d => {
                const mouseCol = d.index;
                return d[mouseCol] || 0;
            });
            
            const colorScale = d3.scaleSequential()
              .interpolator(d3.interpolateYlGnBu)
              .domain([0, maxValue]);
            
            // Create a tooltip
            const tooltip = d3.select("#heatmapContainer")
              .append("div")
                .style("opacity", 0)
                .attr("class", "tooltip")
                .style("background-color", "white")
                .style("border", "solid")
                .style("border-width", "2px")
                .style("border-radius", "5px")
                .style("padding", "5px")
                .style("position", "absolute");
            
            // Add the heatmap cells
            for (let date of dates) {
                const dateData = mouseHeatmapData.find(d => d.Date === date);
                
                if (dateData) {
                    for (let mouse of mice) {
                        const value = dateData[mouse] || 0;
                        
                        svg.append("rect")
                            .attr("x", x(mouse))
                            .attr("y", y(date))
                            .attr("width", x.bandwidth())
                            .attr("height", y.bandwidth())
                            .attr("class", "heatmap-cell")
                            .style("fill", value === 0 ? "#f8f9fa" : colorScale(value))
                            .on("mouseover", function(event) {
                                tooltip.style("opacity", 1);
                                d3.select(this)
                                    .style("stroke", "black")
                                    .style("stroke-width", "2px");
                            })
                            .on("mousemove", function(event) {
                                tooltip
                                    .html(`Date: ${date}<br>Mouse: ${mouse}<br>Sessions: ${value}`)
                                    .style("left", (event.pageX + 10) + "px")
                                    .style("top", (event.pageY - 20) + "px");
                            })
                            .on("mouseleave", function() {
                                tooltip.style("opacity", 0);
                                d3.select(this)
                                    .style("stroke", "white")
                                    .style("stroke-width", "1px");
                            });
                        
                        // Add text for non-zero values
                        if (value > 0) {
                            svg.append("text")
                                .attr("x", x(mouse) + x.bandwidth()/2)
                                .attr("y", y(date) + y.bandwidth()/2)
                                .attr("text-anchor", "middle")
                                .attr("dominant-baseline", "central")
                                .style("font-size", "12px")
                                .style("fill", value > maxValue/2 ? "white" : "black")
                                .text(value);
                        }
                    }
                }
            }
        }
        
        // Initialize DataTables for session tables
        function initializeSessionTables() {
            // All sessions table
            $('#allSessionsTable').DataTable({
                data: sessionDetailsData,
                columns: [
                    { data: 'Date' },
                    { data: 'Time' },
                    { data: 'Mouse' },
                    { data: 'Session ID' },
                    { 
                        data: 'Phase',
                        render: function(data) {
                            return `<span class="badge phase-${data}">${data}</span>`;
                        }
                    },
                    { data: 'Total Trials' },
                    { data: 'Video Length (min)' },
                    { 
                        data: null,
                        render: function(data) {
                            return '<button class="btn btn-sm btn-primary view-details" data-session-id="' + 
                                   data['Session ID'] + '">View</button>';
                        }
                    }
                ],
                order: [[0, 'desc'], [1, 'desc']],
                pageLength: 25
            });
            
            // Mouse sessions table (initially empty, populated on mouse selection)
            $('#mouseSessionsTable').DataTable({
                columns: [
                    { data: 'Date' },
                    { data: 'Time' },
                    { data: 'Session ID' },
                    { 
                        data: 'Phase',
                        render: function(data) {
                            return `<span class="badge phase-${data}">${data}</span>`;
                        }
                    },
                    { data: 'Total Trials' },
                    { data: 'Video Length (min)' }
                ],
                order: [[0, 'desc'], [1, 'desc']]
            });
            
            // Phase sessions table (initially empty, populated on phase selection)
            $('#phaseSessionsTable').DataTable({
                columns: [
                    { data: 'Date' },
                    { data: 'Time' },
                    { data: 'Mouse' },
                    { data: 'Session ID' },
                    { data: 'Total Trials' },
                    { data: 'Video Length (min)' }
                ],
                order: [[0, 'desc'], [1, 'desc']]
            });
            
            // Set up session details modal
            $('#allSessionsTable').on('click', '.view-details', function() {
                const sessionId = $(this).data('session-id');
                showSessionDetails(sessionId);
            });
        }
        
        // Set up event listeners for interactive elements
        function setupEventListeners() {
            // Mouse selector change event
            mouseSelector.addEventListener('change', function() {
                const selectedMouse = this.value;
                updateMouseAnalysis(selectedMouse);
            });
            
            // Phase selector change event
            phaseSelector.addEventListener('change', function() {
                const selectedPhase = this.value;
                updatePhaseAnalysis(selectedPhase);
            });
            
            // Month selector change event
            monthSelector.addEventListener('change', function() {
                const selectedMonth = this.value;
                updateHeatmapByMonth(selectedMonth);
            });
            
            // Apply filters button
            document.getElementById('applyFilters').addEventListener('click', function() {
                applySessionFilters();
            });
            
            // Reset filters button
            document.getElementById('resetFilters').addEventListener('click', function() {
                resetSessionFilters();
            });
            
            // Trigger change events for default selections
            if (mouseSelector.options.length > 0) {
                updateMouseAnalysis(mouseSelector.value);
            }
            
            if (phaseSelector.options.length > 0) {
                updatePhaseAnalysis(phaseSelector.value);
            }
        }
        
        // Update mouse analysis section
        function updateMouseAnalysis(mouseId) {
            // Update mouse progression chart
            updateMouseProgressionChart(mouseId);
            
            // Update mouse sessions table
            updateMouseSessionsTable(mouseId);
            
            // Update mouse calendar
            updateMouseCalendar(mouseId);
        }
        
        // Update mouse progression chart
        function updateMouseProgressionChart(mouseId) {
            // Filter data for the selected mouse
            const mouseData = mouseProgressionData.filter(d => d.Mouse === mouseId);
            
            // Group by phase
            const phaseGroups = {};
            mouseData.forEach(d => {
                if (!phaseGroups[d.Phase]) {
                    phaseGroups[d.Phase] = [];
                }
                phaseGroups[d.Phase].push({
                    x: new Date(d.Date),
                    y: d.Phase
                });
            });
            
            // Create datasets
            const datasets = [];
            const phaseColors = {
                '1': '#007bff',
                '2': '#28a745',
                '3': '#17a2b8',
                '4': '#ffc107',
                '5': '#dc3545',
                '6': '#6610f2',
                '7': '#fd7e14',
                '8': '#20c997',
                '9': '#e83e8c',
                '10': '#6f42c1',
                '3b': '#138496',
                '4b': '#d39e00',
                'test': '#6c757d'
            };
            
            Object.keys(phaseGroups).forEach(phase => {
                datasets.push({
                    label: `Phase ${phase}`,
                    data: phaseGroups[phase],
                    backgroundColor: phaseColors[phase] || '#6c757d',
                    borderColor: phaseColors[phase] || '#6c757d',
                    pointRadius: 6,
                    pointHoverRadius: 8
                });
            });
            
            // Add connecting line dataset if there's data
            if (mouseData.length > 0) {
                const sortedData = [...mouseData].sort((a, b) => 
                    new Date(a.Date) - new Date(b.Date));
                
                datasets.push({
                    label: 'Progression',
                    data: sortedData.map(d => ({
                        x: new Date(d.Date),
                        y: d.Phase
                    })),
                    backgroundColor: 'rgba(0,0,0,0.1)',
                    borderColor: 'rgba(0,0,0,0.2)',
                    borderWidth: 1,
                    borderDash: [5, 5],
                    pointRadius: 0,
                    fill: false,
                    showLine: true
                });
            }
            
            // Update chart
            mouseProgressionChart.data.datasets = datasets;
            mouseProgressionChart.update();
        }
        
        // Update mouse sessions table
        function updateMouseSessionsTable(mouseId) {
            const mouseData = sessionDetailsData.filter(d => d.Mouse === mouseId);
            $('#mouseSessionsTable').DataTable().clear().rows.add(mouseData).draw();
        }
        
        // Update mouse calendar
        function updateMouseCalendar(mouseId) {
            // Create a calendar-like visualization for the mouse
            const calendarContainer = document.getElementById('mouseCalendarContainer');
            calendarContainer.innerHTML = '';
            
            // Filter sessions for this mouse
            const mouseSessions = sessionDetailsData.filter(d => d.Mouse === mouseId);
            
            // Group by month and date
            const sessionsByMonth = {};
            mouseSessions.forEach(session => {
                const date = new Date(session.Date);
                const year = date.getFullYear();
                const month = date.getMonth();
                const key = `${year}-${month}`;
                
                if (!sessionsByMonth[key]) {
                    sessionsByMonth[key] = {
                        year: year,
                        month: month,
                        sessions: {}
                    };
                }
                
                const day = date.getDate();
                if (!sessionsByMonth[key].sessions[day]) {
                    sessionsByMonth[key].sessions[day] = [];
                }
                
                sessionsByMonth[key].sessions[day].push(session);
            });
            
            // Create month calendars
            Object.values(sessionsByMonth).sort((a, b) => {
                return a.year !== b.year ? a.year - b.year : a.month - b.month;
            }).forEach(monthData => {
                createMonthCalendar(calendarContainer, monthData, mouseId);
            });
        }
        
        // Create a month calendar
        function createMonthCalendar(container, monthData, mouseId) {
            const monthNames = [
                'January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December'
            ];
            
            // Create month container
            const monthContainer = document.createElement('div');
            monthContainer.className = 'card mb-3';
            
            // Create header
            const header = document.createElement('div');
            header.className = 'card-header';
            header.innerHTML = `${monthNames[monthData.month]} ${monthData.year}`;
            monthContainer.appendChild(header);
            
            // Create calendar body
            const calendar = document.createElement('div');
            calendar.className = 'card-body p-2';
            
            // Create table
            const table = document.createElement('table');
            table.className = 'table table-bordered';
            
            // Create header row with day names
            const thead = document.createElement('thead');
            const headerRow = document.createElement('tr');
            ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].forEach(day => {
                const th = document.createElement('th');
                th.className = 'text-center';
                th.textContent = day;
                headerRow.appendChild(th);
            });
            thead.appendChild(headerRow);
            table.appendChild(thead);
            
            // Create calendar body
            const tbody = document.createElement('tbody');
            
            // Get first day of month and last day
            const firstDay = new Date(monthData.year, monthData.month, 1);
            const lastDay = new Date(monthData.year, monthData.month + 1, 0);
            
            let day = 1;
            let currentWeek = document.createElement('tr');
            
            // Empty cells for days before the first day of month
            for (let i = 0; i < firstDay.getDay(); i++) {
                const td = document.createElement('td');
                td.className = 'text-center text-muted bg-light';
                currentWeek.appendChild(td);
            }
            
            // Cells for each day of the month
            while (day <= lastDay.getDate()) {
                // If we've reached the end of a week, start a new row
                if (firstDay.getDay() + day - 1 > 6 && (firstDay.getDay() + day - 1) % 7 === 0) {
                    tbody.appendChild(currentWeek);
                    currentWeek = document.createElement('tr');
                }
                
                const td = document.createElement('td');
                td.className = 'text-center';
                
                // Check if there are sessions on this day
                const daySessions = monthData.sessions[day] || [];
                
                if (daySessions.length > 0) {
                    // Day with sessions
                    td.classList.add('bg-primary', 'text-white');
                    
                    // Create a badge with session count if more than 1
                    if (daySessions.length > 1) {
                        td.innerHTML = `${day} <span class="badge bg-white text-primary">${daySessions.length}</span>`;
                    } else {
                        td.textContent = day;
                    }
                    
                    // Add tooltip with session details
                    td.setAttribute('title', `${daySessions.length} session(s)`);
                    td.style.cursor = 'pointer';
                    
                    // Add click event to show sessions for this day
                    td.addEventListener('click', function() {
                        // Format date for display
                        const formattedDate = new Date(monthData.year, monthData.month, day)
                            .toISOString().split('T')[0];
                        
                        // Filter and display sessions for this day and mouse
                        const dayMouseSessions = sessionDetailsData.filter(
                            s => s.Date === formattedDate && s.Mouse === mouseId
                        );
                        
                        // Show modal with sessions
                        showDaySessionsModal(formattedDate, mouseId, dayMouseSessions);
                    });
                } else {
                    // Day without sessions
                    td.textContent = day;
                }
                
                currentWeek.appendChild(td);
                day++;
            }
            
            // Fill remaining cells in the last week
            const remainingCells = 7 - currentWeek.children.length;
            for (let i = 0; i < remainingCells; i++) {
                const td = document.createElement('td');
                td.className = 'text-center text-muted bg-light';
                currentWeek.appendChild(td);
            }
            
            tbody.appendChild(currentWeek);
            table.appendChild(tbody);
            calendar.appendChild(table);
            monthContainer.appendChild(calendar);
            container.appendChild(monthContainer);
        }
        
        // Show modal with sessions for a specific day
        function showDaySessionsModal(date, mouseId, sessions) {
            const modal = new bootstrap.Modal(document.getElementById('sessionDetailsModal'));
            const modalTitle = document.getElementById('sessionModalLabel');
            const modalBody = document.getElementById('sessionModalBody');
            
            modalTitle.textContent = `Sessions for ${mouseId} on ${date}`;
            
            // Create table with session details
            let content = `
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>Time</th>
                            <th>Session ID</th>
                            <th>Phase</th>
                            <th>Trials</th>
                            <th>Video Length</th>
                        </tr>
                    </thead>
                    <tbody>
            `;
            
            sessions.forEach(session => {
                content += `
                    <tr>
                        <td>${session.Time}</td>
                        <td>${session['Session ID']}</td>
                        <td><span class="badge phase-${session.Phase}">Phase ${session.Phase}</span></td>
                        <td>${session['Total Trials'] || 'N/A'}</td>
                        <td>${session['Video Length (min)'] || 'N/A'}</td>
                    </tr>
                `;
            });
            
            content += `
                    </tbody>
                </table>
            `;
            
            modalBody.innerHTML = content;
            modal.show();
        }
        
        // Update phase analysis section
        function updatePhaseAnalysis(phase) {
            // Filter sessions for this phase
            const phaseSessions = sessionDetailsData.filter(d => d.Phase == phase);
            
            // Update sessions table
            $('#phaseSessionsTable').DataTable().clear().rows.add(phaseSessions).draw();
            
            // Update mice distribution chart
            updatePhaseDistributionByMice(phase);
            
            // Update phase timeline chart
            updatePhaseTimeline(phase);
        }
        
        // Update mice distribution chart for a specific phase
        function updatePhaseDistributionByMice(phase) {
            // Count sessions by mouse for this phase
            const phaseSessions = sessionDetailsData.filter(d => d.Phase == phase);
            
            const mouseSessionCounts = {};
            phaseSessions.forEach(session => {
                const mouse = session.Mouse;
                mouseSessionCounts[mouse] = (mouseSessionCounts[mouse] || 0) + 1;
            });
            
            // Convert to chart data
            const labels = Object.keys(mouseSessionCounts);
            const data = Object.values(mouseSessionCounts);
            
            // Generate random colors for each mouse
            const colors = labels.map((_, index) => {
                const hue = (360 * index / labels.length) % 360;
                return `hsl(${hue}, 70%, 60%)`;
            });
            
            // Update chart
            phaseDistributionByMiceChart.data.labels = labels;
            phaseDistributionByMiceChart.data.datasets[0].data = data;
            phaseDistributionByMiceChart.data.datasets[0].backgroundColor = colors;
            phaseDistributionByMiceChart.update();
        }
        
        // Update phase timeline chart
        function updatePhaseTimeline(phase) {
            // Filter sessions for this phase
            const phaseSessions = sessionDetailsData.filter(d => d.Phase == phase);
            
            // Group sessions by date
            const sessionsByDate = {};
            phaseSessions.forEach(session => {
                const date = session.Date;
                if (!sessionsByDate[date]) {
                    sessionsByDate[date] = 0;
                }
                sessionsByDate[date]++;
            });
            
            // Convert to sorted arrays for chart
            const dates = Object.keys(sessionsByDate).sort();
            const counts = dates.map(date => sessionsByDate[date]);
            
            // Update chart
            phaseTimelineChart.data.labels = dates;
            phaseTimelineChart.data.datasets[0].data = counts;
            phaseTimelineChart.options.scales.y.title.text = 'Sessions in Phase ' + phase;
            phaseTimelineChart.update();
        }
        
        // Update heatmap by month filter
        function updateHeatmapByMonth(month) {
            // Filter data by selected month
            let filteredData;
            
            if (month === 'all') {
                filteredData = [...mouseHeatmapData];
            } else {
                filteredData = mouseHeatmapData.filter(d => d.Date.startsWith(month));
            }
            
            // Update heatmap with filtered data
            // (This would require rebuilding the heatmap - for simplicity, we'll just log this)
            console.log(`Updated heatmap to show month: ${month}`);
            // In a real implementation, you'd rebuild the heatmap here
        }
        
        // Apply filters to session explorer
        function applySessionFilters() {
            const startDate = document.getElementById('startDateFilter').value;
            const endDate = document.getElementById('endDateFilter').value;
            const mouseFilter = getMultiSelectValues('mouseFilter');
            const phaseFilter = getMultiSelectValues('phaseFilter');
            
            // Get the DataTable instance
            const table = $('#allSessionsTable').DataTable();
            
            // Clear existing filters
            table.search('').columns().search('').draw();
            
            // Apply date filter
            if (startDate && endDate) {
                $.fn.dataTable.ext.search.push(
                    function(settings, data, dataIndex) {
                        const sessionDate = data[0]; // 'Date' column
                        return sessionDate >= startDate && sessionDate <= endDate;
                    }
                );
            }
            
            // Apply mouse filter
            if (!mouseFilter.includes('all')) {
                table.column(2) // 'Mouse' column
                    .search(mouseFilter.join('|'), true, false)
                    .draw();
            }
            
            // Apply phase filter
            if (!phaseFilter.includes('all')) {
                table.column(4) // 'Phase' column
                    .search(phaseFilter.join('|'), true, false)
                    .draw();
            }
            
            // Redraw the table
            table.draw();
        }
        
        // Reset all filters
        function resetSessionFilters() {
            // Reset date inputs
            document.getElementById('startDateFilter').value = '';
            document.getElementById('endDateFilter').value = '';
            
            // Reset mouse filters
            resetMultiSelect('mouseFilter');
            
            // Reset phase filters
            resetMultiSelect('phaseFilter');
            
            // Clear all DataTable filters
            const table = $('#allSessionsTable').DataTable();
            $.fn.dataTable.ext.search.pop(); // Remove date filter
            table.search('').columns().search('').draw();
        }
        
        // Helper function to get values from a multi-select element
        function getMultiSelectValues(elementId) {
            const select = document.getElementById(elementId);
            const result = [];
            const options = select.options;
            
            for (let i = 0; i < options.length; i++) {
                if (options[i].selected) {
                    result.push(options[i].value);
                }
            }
            
            return result;
        }
        
        // Helper function to reset a multi-select element
        function resetMultiSelect(elementId) {
            const select = document.getElementById(elementId);
            const options = select.options;
            
            for (let i = 0; i < options.length; i++) {
                if (options[i].value === 'all') {
                    options[i].selected = true;
                } else {
                    options[i].selected = false;
                }
            }
        }
        
        // Show details for a specific session
        function showSessionDetails(sessionId) {
            // Find the session in the data
            const session = sessionDetailsData.find(s => s['Session ID'] === sessionId);
            
            if (!session) {
                console.error(`Session not found: ${sessionId}`);
                return;
            }
            
            // Set up modal
            const modal = new bootstrap.Modal(document.getElementById('sessionDetailsModal'));
            const modalTitle = document.getElementById('sessionModalLabel');
            const modalBody = document.getElementById('sessionModalBody');
            
            modalTitle.textContent = `Session Details: ${sessionId}`;
            
            // Create content
            let content = `
                <div class="row">
                    <div class="col-md-6">
                        <div class="mb-3">
                            <strong>Date:</strong> ${session.Date}
                        </div>
                        <div class="mb-3">
                            <strong>Time:</strong> ${session.Time}
                        </div>
                        <div class="mb-3">
                            <strong>Mouse:</strong> ${session.Mouse}
                        </div>
                        <div class="mb-3">
                            <strong>Phase:</strong> <span class="badge phase-${session.Phase}">${session.Phase}</span>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="mb-3">
                            <strong>Total Trials:</strong> ${session['Total Trials'] || 'N/A'}
                        </div>
                        <div class="mb-3">
                            <strong>Video Length:</strong> ${session['Video Length (min)'] || 'N/A'} min
                        </div>
                        <div class="mb-3">
                            <strong>Is Complete:</strong> ${session['Is Complete'] ? 'Yes' : 'No'}
                        </div>
                    </div>
                </div>
                
                <div class="row mt-3">
                    <div class="col-12">
                        <h5>Session Path</h5>
                        <code>${session.directory || 'N/A'}</code>
                    </div>
                </div>
            `;
            
            modalBody.innerHTML = content;
            modal.show();
        }
        
        // Helper function to get colors for phases
        function getPhaseColors(phases) {
            const phaseColors = {
                '1': '#007bff',
                '2': '#28a745',
                '3': '#17a2b8',
                '4': '#ffc107',
                '5': '#dc3545',
                '6': '#6610f2',
                '7': '#fd7e14',
                '8': '#20c997',
                '9': '#e83e8c',
                '10': '#6f42c1',
                '3b': '#138496',
                '4b': '#d39e00',
                'test': '#6c757d'
            };
            
            return phases.map(phase => phaseColors[phase] || '#6c757d');
        }
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
    return template + JAVASCRIPT_TEMPLATE