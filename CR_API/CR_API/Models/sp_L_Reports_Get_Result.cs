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
    
    public partial class sp_L_Reports_Get_Result
    {
        public System.Guid ReportID { get; set; }
        public string ReportName { get; set; }
        public string Description { get; set; }
        public string Category { get; set; }
        public Nullable<bool> IsOnScreen { get; set; }
        public string DEV { get; set; }
        public string Location { get; set; }
        public Nullable<System.DateTime> CreatedOn { get; set; }
        public string CreatedBy { get; set; }
        public Nullable<System.DateTime> ModifiedOn { get; set; }
        public string ModifiedBy { get; set; }
        public string NotesTester { get; set; }
    }
}
