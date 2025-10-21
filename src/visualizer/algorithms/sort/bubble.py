import plotly.graph_objects as go


def bubble(arr: list[int]) -> None:
    x = list(range(len(arr)))
    frames = []
    a = arr.copy()
    n = len(a)

    # Generate frames for each step
    for i in range(n):
        for j in range(0, n - i - 1):
            # Highlight compared bars
            colors = ["skyblue"] * n
            colors[j], colors[j + 1] = "orange", "orange"

            # Add frame before possible swap
            frames.append(
                go.Frame(data=[go.Bar(x=x, y=a, marker_color=colors)], name=f"{i}-{j}")
            )

            # Swap if needed
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

                # Add frame after swap
                frames.append(
                    go.Frame(
                        data=[go.Bar(x=x, y=a, marker_color=colors)],
                        name=f"swap-{i}-{j}",
                    )
                )

    # Final frame (sorted)
    frames.append(
        go.Frame(
            data=[go.Bar(x=x, y=a, marker_color=["lightgreen"] * n)], name="sorted"
        )
    )

    # Create initial figure
    fig = go.Figure(
        data=[go.Bar(x=x, y=arr, marker_color="skyblue")],
        layout=go.Layout(
            title="Bubble Sort Animation",
            xaxis=dict(title="Index"),
            yaxis=dict(title="Value"),
            bargap=0.2,
            updatemenus=[
                {
                    "buttons": [
                        {
                            "args": [
                                None,
                                {
                                    "frame": {"duration": 200, "redraw": True},
                                    "fromcurrent": True,
                                },
                            ],
                            "label": "▶ Play",
                            "method": "animate",
                        },
                        {
                            "args": [
                                [None],
                                {
                                    "frame": {"duration": 0},
                                    "mode": "immediate",
                                    "transition": {"duration": 0},
                                },
                            ],
                            "label": "⏸ Pause",
                            "method": "animate",
                        },
                    ],
                    "direction": "left",
                    "pad": {"r": 10, "t": 60},
                    "showactive": False,
                    "type": "buttons",
                    "x": 0.1,
                    "xanchor": "right",
                    "y": 0,
                    "yanchor": "top",
                }
            ],
        ),
        frames=frames,
    )

    fig.show()
