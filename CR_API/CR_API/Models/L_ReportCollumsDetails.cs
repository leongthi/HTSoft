//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace CR_API.Models
{
    using System;
    using System.Collections.Generic;
    
    public partial class L_ReportCollumsDetails
    {
        public System.Guid ReportID { get; set; }
        public int ID { get; set; }
        public int CollumIndex { get; set; }
        public Nullable<int> STT { get; set; }
        public Nullable<int> TableNo { get; set; }
        public string CollumName { get; set; }
        public string FontSize { get; set; }
        public string CollumType { get; set; }
        public string Description { get; set; }
        public string DevDescription { get; set; }
        public string Notes { get; set; }
        public string Table { get; set; }
        public string Field { get; set; }
        public string Dev_Type { get; set; }
        public Nullable<System.DateTime> CreatedOn { get; set; }
        public string CreatedBy { get; set; }
        public Nullable<System.DateTime> ModifiedOn { get; set; }
        public string ModifiedBy { get; set; }
    }
}