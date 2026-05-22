import { useEffect, useState } from "react";
import api from "../services/api";

export default function Dashboard() {
  const [stats, setStats] = useState(null);
  const [flows, setFlows] = useState([]);

  useEffect(() => {
    api.get("/stats").then((res) => {
      setStats(res.data);
    });

    api.get("/flows").then((res) => {
      setFlows(res.data);
    });
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>DPI Dashboard</h1>

      {stats && (
        <div>
          <h2>Total Packets: {stats.total_packets}</h2>
          <h2>Blocked: {stats.blocked}</h2>
        </div>
      )}

      <h2>Flows</h2>

      <table border="1">
        <thead>
          <tr>
            <th>Source</th>
            <th>Destination</th>
            <th>App</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {flows.map((flow, index) => (
            <tr key={index}>
              <td>{flow.src_ip}</td>
              <td>{flow.dst_ip}</td>
              <td>{flow.app_type}</td>
              <td>
                {flow.blocked ? "BLOCKED" : "ALLOWED"}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
