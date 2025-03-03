import { Beaker, PackageOpen } from "lucide-react";
import { motion } from "framer-motion";

export default function OverviewSection() {
  const data = [
    { label: "Total Labs", value: 3, icon: <Beaker strokeWidth={1.5} /> },
    {
      label: "Total Resources",
      value: 4,
      icon: <PackageOpen strokeWidth={1.5} />,
    },
    { label: "Active Bookings", value: 2, icon: <Beaker strokeWidth={1.5} /> },
    {
      label: "Pending Requests",
      value: 1,
      icon: <PackageOpen strokeWidth={1.5} />,
    },
  ];

  return (
    <div className="overview-section">
      {data.map((item, index) => (
        <div key={index} className="overview-card">
          <div className="overview-card-upper">
            <div className="overview-card-label">{item.label}</div>
            <div className="overview-card-icon">{item.icon}</div>
          </div>
          <div className="overview-card-content">{item.value}</div>
        </div>
      ))}
    </div>
  );
}