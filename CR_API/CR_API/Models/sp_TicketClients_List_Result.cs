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
    
    public partial class sp_TicketClients_List_Result
    {
        public int ClientID { get; set; }
        public string ClientName { get; set; }
        public string Priority { get; set; }
        public Nullable<System.DateTime> DueDate { get; set; }
        public string Status { get; set; }
        public Nullable<System.DateTime> CreatedOn { get; set; }
        public string CreatedBy { get; set; }
        public Nullable<System.DateTime> ModifiedOn { get; set; }
        public string ModifiedBy { get; set; }
        public Nullable<bool> IsDeployed { get; set; }
    }
}
