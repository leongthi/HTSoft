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
    
    public partial class ws_Ticket_Hotfix_Result
    {
        public int TicketID { get; set; }
        public string TicketEmailID { get; set; }
        public string Priority { get; set; }
        public string Status { get; set; }
        public Nullable<System.DateTime> DueDate { get; set; }
        public Nullable<int> AssignedTo { get; set; }
        public string Title { get; set; }
        public string Title_Ununicode { get; set; }
        public string Description { get; set; }
        public Nullable<int> CreatedDateAsInt { get; set; }
        public Nullable<System.DateTime> CreatedOn { get; set; }
        public string CreatedBy { get; set; }
        public Nullable<System.DateTime> ModifiedOn { get; set; }
        public string ModifiedBy { get; set; }
        public Nullable<System.DateTime> CompletedOn { get; set; }
        public string Responsibility { get; set; }
        public string Category { get; set; }
        public string MODULE { get; set; }
        public string RequestedBy { get; set; }
        public Nullable<int> RequestedBy_CheckSum { get; set; }
        public Nullable<int> TeamID { get; set; }
        public Nullable<int> PrimaryDEV { get; set; }
        public Nullable<int> PrimaryQC { get; set; }
        public string Comment { get; set; }
        public Nullable<System.DateTime> OrginalDeadline { get; set; }
        public Nullable<System.Guid> ReportID { get; set; }
        public string TypeScripts { get; set; }
        public Nullable<int> ProjectID { get; set; }
        public Nullable<int> RequestStatus { get; set; }
        public Nullable<int> ParentTicketID { get; set; }
        public Nullable<bool> IsParent { get; set; }
        public string ReportedBy { get; set; }
        public string ReleaseNote { get; set; }
        public Nullable<int> PrimaryBA { get; set; }
        public Nullable<int> TicketOwner { get; set; }
        public Nullable<System.DateTime> Reproduce { get; set; }
        public Nullable<System.Guid> DocumentID { get; set; }
    }
}