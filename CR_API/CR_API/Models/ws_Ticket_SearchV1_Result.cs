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
    
    public partial class ws_Ticket_SearchV1_Result
    {
        public string Title { get; set; }
        public int TicketID { get; set; }
        public string Status { get; set; }
        public string Responsibility { get; set; }
        public string RequestedBy { get; set; }
        public string Priority { get; set; }
        public string MODULE { get; set; }
        public Nullable<System.DateTime> ModifiedOn { get; set; }
        public string ModifiedBy { get; set; }
        public Nullable<System.DateTime> DueDate { get; set; }
        public string Description { get; set; }
        public Nullable<System.DateTime> CreatedOn { get; set; }
        public string CreatedBy { get; set; }
        public Nullable<System.DateTime> CompletedOn { get; set; }
        public string Category { get; set; }
        public Nullable<int> AssignedTo { get; set; }
        public int BuildID { get; set; }
        public string BuildName { get; set; }
        public string BuildDueDate { get; set; }
        public string StatusBuild { get; set; }
        public int ID { get; set; }
        public string Responsibility1 { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Email { get; set; }
        public string AssignedToName { get; set; }
        public string ForeColor { get; set; }
        public string ClientName { get; set; }
        public int PercentComplete { get; set; }
        public int IsFollow { get; set; }
        public string ProjectName { get; set; }
        public Nullable<int> ParentTicketID { get; set; }
    }
}